import streamlit as st
from PIL import Image
import api
import pandas as pd
import numpy as np
from datetime import datetime
import random

map = Image.open(r"C:\Users\48694\Desktop\CSstudies\PersonalProjects\WhereToSwitz\SwitzCantons.jpg")
HOURS = ('6:00', '9:00', '12:00', '15:00', '18:00', '21:00')

st.title('WhereToSwitz - Where is a good weather in Switzerland!')
st.subheader('Map of Switzerland Cantons')
st.image(map)

day_option = st.selectbox(
   'Choose a day:',
   ('Today', 'Tomorrow', 'The day after tomorrow'))

if day_option in ('Tomorrow', 'The day after tomorrow'):
   time_option = st.selectbox('Choose a time:', HOURS)
else:
   now = datetime.now()
   selected_hours = tuple([h for h in HOURS if now.hour < int(h.split(":")[0])])
   if selected_hours:
      time_option = st.selectbox('Choose a time:', selected_hours)
   else:
      st.text('Check tomorrow')

weather_option = st.selectbox(
   'Choose a weather you are interested in:',
   ('-', 'Sun', 'Clouds', 'Rain/Snow'))
# https://openweathermap.org/weather-conditions - this data are going to be helpful to map it all 

st.header("Overview")
st.dataframe(
   api.cantonal_data_df,
   column_config={
   "Icon": st.column_config.ImageColumn(),
   },
   hide_index=True,
   use_container_width=True,
   height=945,
)


# for key, val in api.canton_capital_dict.items():
#     st.write(key, val)

# TO DO
# catch the data to not to call them every time
# add the insight for the different hours
# add the possible the weather in the next 3 days as well 
# You can add functionality to look for a specyfic cities 
