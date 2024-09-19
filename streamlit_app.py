import streamlit as st
import pandas as pd

st.title('🎈 ml app')
st.info('this is a machine learning mapp')

st.write('Hello world!')


with st.expander('Data'):
  st.write('**Raw Data**') # using the markdown here
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df  
  
  st.write('**X**')   
  X = df.drop('species', axis=1)
  X
  
  st.write('**Y**')
  Y = df[['species']]
  Y
  
with st.expander('Data visualization'):
  # referring to https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart please
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

