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
  X_raw = df.drop('species', axis=1)
  X_raw
  
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
  # the third value is the default value lol
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)

  # the dataframe for the input features
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}
  input_df = pd.DataFrame(data, index=[0]) 
  input_df

  input_penguins = pd.concat([input_df, X_raw], axis=0)
  input_penguins
with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguins data**')
  input_penguins
  # encode
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
# refer to https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-dummies

with st.expander('dummies'):
  st.write('**here we are**')
  df_penguins
  
X = df_penguins[1:]
input_row = df_penguins[:1]

# Encode y
target_mapper = {'Adelie': 0,
                 'Chinstrap': 1,
                 'Gentoo': 2}
def target_encode(val):
  return target_mapper[val]

y = Y.apply(target_encode)
