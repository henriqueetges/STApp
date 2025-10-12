import streamlit as st

st.set_page_config(page_title="Data Engineering Porfolio", page_icon="📊")

st.write("# Meu Portfolio em Data Engineering #")
st.sidebar.header("Databricks")

st.markdown("""Aqui estão reunidos algums projetos de portfolio. O que se encontra aqui é somente uma parte do meu trabalho, usando dados de disponibilidade
            pública na web""")


page_selected = st.sidebar.selectbox("Samples:", ['Brapi data', 'Data Integrity with Pyspark', 'DLT'])

if page_selected == 'Brapi data':
    st.title("Brapi data - Medallion Architecture")
    st.write("""
             This project was aimed at keeping a medallion architecture using databricks, while pulling stock ticker prices from Brapi's API.
             
             Data flows from the API calls into bronze layer, in silver we perform data schema validations and other data quality validations. 
             
             The project is available at: https://github.com/henriqueetges/MyDatalake
             
             """
             
             )
elif page_selected == 'Data Integrity with Pyspark':
    st.title("Data Integrity with Pyspark")
    st.write("""
             This project is part of my sandbox datalake implementation, and the goal if it is to perform data quality checks in my data to assess its
             
             quality scores based on the five Quality Dimensions Framework (Timeliness, Completeness, Uniqueness, Validity and Consistency)
             
             In this project I tried creating a two scoring modules:
             - *Checker* - Its the main component, which takes each of datasets and performs the individual tests. Contains all of the pyspark testing logic.
             After running the checks, it saves it into another table for reporting purposes.
             
             - *CheckerHandler* - Takes a list of datasets locations, a path to the yml file defining schema and tests to be performed. From this
             it calls the Checker in each of them to analyze the rules 
             
             Since this project has been included into my DataLake project implementation, I haven't been maintaining its individual repository.
             But you can find some information about the project here: https://github.com/henriqueetges/MyExpectations
             """)

elif page_selected == 'DLT':
    
    st.title("DLT")
    st.write("""
            This is another piece of my Datalake implementation, where I am slowly transitioning the ELT/ETL scripts from normal batch operations
            into DLT pipelines in Databricks.
            
            You can find some examples in my DataLake repository, here: https://github.com/henriqueetges/MyDatalake
             """)
