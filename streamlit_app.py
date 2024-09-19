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


# more data preparation
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('male', 'female'))
  
  # kinda like an option of range 
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)

