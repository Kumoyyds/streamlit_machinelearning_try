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
