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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# takes the jason version to normalize the data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# displays the dataframe
streamlit.dataframe(fruityvice_normalized)
