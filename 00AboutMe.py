import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

st.set_page_config(
    page_title="Henrique Pedro Etges",
    page_icon="⚽"
)   

if "language_selected" not in st.session_state:
    st.session_state.language_selected = 'en-US'
    
language_selection = st.pills(label='', options=['en-US', 'pt-BR'], default=st.session_state.language_selected)
st.session_state.language_selected = language_selection
    
with open("content\home.json", "r",encoding='UTF-8') as f:
    data = json.load(f)
content = data['languages'][st.session_state.language_selected]

with st.container():
    st.html(f"""
       <div style="background-color: #701f57; padding: 20px; border-radius: 10px;">
           <h1>{content['Heading']}!</h1>
           <p>{content['About Me']}</p>
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

    
st.markdown(f"{content['Curriculum']}")

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
