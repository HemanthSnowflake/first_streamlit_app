
import streamlit
import pandas


streamlit.title('Healthy Eating for everyone')

streamlit.header('Eat what feels right for you body')
streamlit.text('Whats new here')

    

streamlit.header('🥣🥣Breakfast Menu🥣🥣')
streamlit.text('🥗🥗Omega 3 & Blueberry Oatmeal :DD')
streamlit.text('🥑🥑Kale, Spinach & Rocket Smoothie' )
streamlit.text('🐔🐔Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
