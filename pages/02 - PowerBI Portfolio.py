import streamlit as st

st.set_page_config(page_title="PowerBI Porfolio", page_icon="📊")

st.write("# Meu Portfolio em PowerBI #")
st.sidebar.header("Portfolio")

page_selected = st.sidebar.selectbox("Samples:", ['DAX', 'Reports', 'HTML'])
st.write(f"""Aqui estão reunidos algums projetos de portfolio. O que se encontra aqui é somente uma parte do meu trabalho, usando dados de disponibilidade
                pública na web.""")

if page_selected == 'HTML':
    st.title('HTML')
    st.markdown("""
                This include HTML pieces used to create custom visualizations in PowerBI. All of these visualization are HTML + CSS combos used along with
                the HTML Content Visual. Most of these are to created interactive cards.
                Such as:
                - Card with Progress bar: 
                
                ![Card with progress bar](https://raw.githubusercontent.com/henriqueetges/PowerBI---Repo/d49c20896b17b0b795a856572b6654dcb49e84f4/html/card-with-progress-bar/card-with-progress-bar.png)
    
                - card with Progress Bar and delta:
                
                ![Card with progress bar](https://raw.githubusercontent.com/henriqueetges/PowerBI---Repo/d49c20896b17b0b795a856572b6654dcb49e84f4/html/card-with-progress-bar+delta/card-with-progress-bar+delta.png)
                
    """)

elif page_selected == 'DAX':
    st.title('DAX')
    st.write("""
                DAX is the lanagauge used by PowerBI to create measures and calculated columns. It is a descendand from MDX.
                
                Most of the calculations using DAX are simple, but depending on how the data model is set up, we may need to create complex logic definitions
                to calculate some business defined metrics               
                
                """)
    st.markdown("""
                **Historical Active Customers**
                
                This measure calculates the number of customer that were active during the period, by taking into consideration the data selected in the report.
                
                    VAR _minData = MIN(dTempo[DATA])
                    VAR _hoje = TODAY()
                    VAR _resultado = 

                    CALCULATE(
                        DISTINCTCOUNTNOBLANK(dCliente[COD_CLIENTE]),
                        USERELATIONSHIP(dCliente[DATA_CADASTRO], dTempo[DATA]),
                        USERELATIONSHIP(dCliente[COD_REPRE], dRepresentantes[COD_ESTRUTURA]),
                        dCliente[STATUS_ATIVIDADE] = "Ativo"
                        , Filter(
                            ALL( dTempo[DATA] ),
                            dTempo[DATA] <= max(Faturamento[PERIODO]) 
                            )
                    )
                    RETURN 
                    SWITCH(
                        TRUE(),
                        _minData < _hoje && or(ISFILTERED(dRepresentantes), ISINSCOPE(dRepresentantes[NOME_ESTRUTURA])), _resultado
                        _minData >= _hoje, BLANK(), _resultado)

                                    """)
    st.markdown("""
                *ABC Classification of Products*
                
                This measure clalculatges the ABC curve for products sold
                
                    IF(
                        HASONEVALUE(
                            dProdutos[Produto]),
                        
                        VAR tVendasProduto = 
                            ADDCOLUMNS(
                                ALLSELECTED(dProdutos[Produto]), 
                                "@VENDAS", [Fat. Bruto])
                        VAR vValorAtual = [Fat. Bruto]
                        VAR vValorTotal = 
                            CALCULATE(
                                [Fat. Bruto], 
                                ALLSELECTED(dProdutos[Produto]))
                        VAR VvENDAS = 
                            FILTER(
                                tVendasProduto,
                                [@VENDAS] >= vValorAtual)
                        VAR vVendasACM = 
                            SUMX(VvENDAS, [@VENDAS])
                        VAR vPercentCumulado = 
                            DIVIDE(vVendasACM, vValorTotal, 0)

                        VAR Classificacao = 
                            SWITCH(
                                TRUE(),
                                ISBLANK(vPercentCumulado), BLANK(),
                                vPercentCumulado <= 0.7, "A",
                                vPercentCumulado <= 0.9, "B", "C")
                        RETURN Classificacao)                    
                """)
    st.markdown("""
                **New Customers**
                
                This measure calculates the number of new clientes, while being dinamic with the filter selection. It requires some other helper measures
                that calculate the data when a customer is expected to be a new client, which I have not included in this example.
                
                    VAR tClientesComPrimeiraCompra = 
                        CALCULATETABLE(                            
                            ADDCOLUMNS(                            
                                FILTER(
                                    VALUES(dCliente[COD_CLIENTE]),
                                    EOMONTH([Data Ref. Novo], 0) >= EOMONTH([Data Ref Cadastro], 0)),   
                                "DataCliNovo", [Data Ref. Novo]),
                                ALLSELECTED(dCliente),           
                                ALLSELECTED(dTempo),
                                ALL(dRepresentantes)
                        )

                        VAR tClientesComLinhagem =                                         
                            TREATAS(                                
                                tClientesComPrimeiraCompra,
                                Faturamento[COD_CLIENTE],
                                dTempo[DATA])

                        VAR vResultado = 
                        CALCULATE(                                  
                            DISTINCTCOUNT(Faturamento[COD_CLIENTE])   
                            , KEEPFILTERS(tClientesComLinhagem))

                        RETURN vResultado
                """)
    st.markdown("""
                
                **Lost Customers**
                
                Calculates the number of lost customers, being dinamic with the fiter in the report.
                
                    VAR _UltimaDataPerda = 
                        CALCULATE(
                            MAX (dTempo[DATA] ), 
                            ALLSELECTED( dTempo[DATA]),
                            ALLSELECTED( dRepresentantes)
                        )

                    VAR _ClientesComDataPerda = 
                        CALCULATETABLE(
                            ADDCOLUMNS(
                                VALUES( Faturamento[COD_CLIENTE] ), 
                                "UltimaData", [Data Ref. Perdidos]), 
                                dTempo[DATA] <= _UltimaDataPerda
                                )
                                
                    VAR _ClientesPerdidos = 
                        FILTER(
                            _ClientesComDataPerda,
                            [UltimaData] IN VALUES(dTempo[DATA])
                        )

                    VAR _Resultado = 
                        COUNTROWS( _ClientesPerdidos )

                    RETURN _Resultado
                """)
    st.markdown("""
                **Recovered Customers**
                
                Calculates the number of recovered customers, being dinamic with filter selection.
                
                                    
                    VAR vDataMin = MIN (dTempo[DATA]) 
                    VAR tClienteDataPerda = 
                    /*  CRIA UMA TABELA QUE PARA CADA CLIENTE CONTÉM A DATA DE PERDA TEMPORÁRIA, INDEPENDENTE DOS FILTROS DE CLIENTE E DE TEMPO */
                    CALCULATETABLE(                                                 
                        ADDCOLUMNS(                                                 
                            VALUES( Faturamento[COD_CLIENTE] ),
                            "DataPerdaTemporaria", 
                            CALCULATE(
                                [Data Ref. Inativo],
                                dTempo[DATA] < vDataMin)
                        ),
                        ALLSELECTED( dCliente ),                                   
                        ALLSELECTED( dTempo ))

                    VAR tClientesComDataPerda =                                     
                    /*  RETIRA OS CLIENTES QUE NÃO TEM DATA DE PERDA */
                    FILTER(
                        tClienteDataPerda,
                        NOT ISBLANK( [DataPerdaTemporaria] )
                    )

                    VAR ClientesAtivos =                                           
                    /* PEGA A DATA DA PRIMEIRA COMPRA DOS CLIENTES NA SELECAO */
                    ADDCOLUMNS(
                        VALUES(Faturamento[COD_CLIENTE]),
                        "MinimaData",
                        CALCULATE(
                            MIN( Faturamento[PERIODO] ), Faturamento[TIPO_FATURAMENTO] = "Vendas")
                    )

                    VAR ClientesRecuperados =                           
                    /* FILTRA OS CLIENTES TEMPORARIAMENTE PERDIDOS AO COMBINAR CLIENTES PERDIDOS POTENCIAIS E CLIENTES ATIVOS E ENTÃO COMPARAR AS DATAS */
                    FILTER(                                                         
                        NATURALINNERJOIN(                                       
                            ClientesAtivos,
                            tClienteDataPerda
                            ), 
                            [MinimaData] > [DataPerdaTemporaria])


                    VAR vResultado =
                    CALCULATE(
                        COUNTROWS(                                                      
                            FILTER(
                            ClientesRecuperados
                    , [Clientes Novos] <> 1)
                        )
                    )
                    RETURN vResultado
                """)
elif page_selected == 'Reports':
    st.title('PowerBI Reports')
    st.markdown("""In here I'll add the public links to sample powerbi reports.

                """)
    st.image('https://as2.ftcdn.net/v2/jpg/00/08/85/67/1000_F_8856770_vGp3qw2viEt06tqIY55EMwOC84nMBC6x.jpg')
