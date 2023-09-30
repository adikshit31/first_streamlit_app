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

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
