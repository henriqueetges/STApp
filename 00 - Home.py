import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Henrique Pedro Etges",
    page_icon="⚽"
)   

with st.container():
    st.html("""
    <div style="background-color: #701f57; padding: 20px; border-radius: 10px;">
        <h1>Welcome to my page!</h1>
        <p>I am Henrique, I currently live in a small city in southern Brazil. I have been working in the BI/Data world for the past 7 or so years, 
        acting both as an internal employee or as a third-party consultant.</p>

        <div style="display: flex; gap: 20px; align-items: center;">
            <a href="https://github.com/henriqueetges" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30" />
            </a>
            <a href="https://www.linkedin.com/in/henriquepetges" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" />
            </a>
        </div>
    </div>
    """)

    
st.markdown("""
            # Education
            #### PUCRS (Jan 2021 - Nov 2022))
            MBA in Technology for business, focus on AI and Data Science
            #### Univates (2017 - 2020)
            Bachelors in Internatioanl Business                        
            #### Merrimack College - (2011-2015)
            Bachelors in Business Administration, major in Finance
            
            # Work Experience
            
            #### Alliance One Brasil - *Data Integrity Specialist* - (May 2025 - Current)
            
            Worked in setting up a framework for data integrity, scoring each of the agronomy datasets
            based on the 5 quality dimensions. Worked on reporting and data analysis.            
            
            #### Dell Techologies - *Business Intelligence Advisor* - (Dec 2021 - April 2025)
            
            Worked on several data projects within the company, starting with VMWare reporting
            up until working to set up automated reports for the core business. 
                                    
            #### Azion - *Data Analyst* - (Jul 2021 - Dec 2021)
            
            Helped set up the data platform for the company, working on creating, documenting, mataining datasets to be used
            by the company. Helped create the KPI's for the different business units.
            
            #### Box Distribuidora - *Data Analyst* - (Jan 2021 - Jun 2021)
            
            Created the data platform of the company, since the ETL's from the source systems up until reporting. 
            Worked closely with the sales department, helping with training and data story telling for each of the personas using the BI dashboards
            
            #### BIMachine - *Head of Data Applications* - (Sep 2018 - Dec 2020)
            
            Worked on the data apps division of the company, creating and implementing data templates
            for our customers. 
            
            # Skills                

            """)

skills = {'SQL': 90, 'Python': 70, 'Pyspark': 60, 'PowerBI': 90}
df = pd.DataFrame(list(skills.items()), columns=['Skill', 'Score']).sort_values(by='Score', ascending=False)

fig, ax= plt.subplots()
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_facecolor((17/255, 17/255, 23/255))
fig.set_facecolor((17/255, 17/255, 23/255))
ax.tick_params(colors='white')
sns.barplot(df, y='Skill', x='Score', ax=ax, orient='h', hue='Skill', palette='rocket')
st.pyplot(fig )
