import streamlit
streamlit.title('My Spouse new healthy lunch')
streamlit.header('Menu')
streamlit.text('🥣 Khichdi')
streamlit.text('🍞Bharta')
streamlit.text('🥑Curd')
streamlit.text('🥗 Salad')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
