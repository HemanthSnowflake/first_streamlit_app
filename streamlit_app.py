
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Healthy Eating for everyone')

streamlit.header('Eat what feels right for you body')
streamlit.text('Whats new here')

    

streamlit.header('🥣🥣Breakfast Menu🥣🥣')
streamlit.text('🥗🥗Omega 3 & Blueberry Oatmeal :DD')
streamlit.text('🥑🥑Kale, Spinach & Rocket Smoothie' )
streamlit.text('🐔🐔Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)



#create a  repeeatable code block called Function
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    
    
## Display the table on the page.
streamlit.header("Fruityvice Fruit Advice!")


try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
         streamlit.error("Please select a fruit to get info")
    else:
         back_from_function = get_fruitvice_data(fruit_choice)
         streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()

 #       streamlit.write('The user entered ', fruit_choice)

#New Section for Fruitwise API response





#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# Normalise the o/p 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
##Printout
#streamlit.dataframe(fruityvice_normalized)

#Snowflake
#dont run anything till we trouble shoot



streamlit.header("My fruit load list Contains")

#snowflake related Function
def get_fruit_load_list(): 
    with my_cnx.cursor() as my_cur:  
         my_cur.execute("SELECT * from fruit_load_list")
         return my_cur.fetchall()  

#Add a button to load the list    
if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)



# Allow end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute(" insert into fruit_load_list values ('from Streamlit')")
        return "Thanks for adding" + new_fruit
    
add_my_fruit = streamlit.text_input('What fruit would you like to add?') 
if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)

streamlit.stop()

