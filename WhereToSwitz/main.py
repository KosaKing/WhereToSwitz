import streamlit as st
from PIL import Image
import api

map = Image.open(r"C:\Users\48694\Desktop\CSstudies\PersonalProjects\WhereToSwitz\SwitzCantons.jpg")

st.title('WhereToSwitz - Where is a good weather in Switzerland!')
st.subheader('Map of Switzerland Cantons')

st.image(map)


# TO DO
# catch the data to not to call them every time
# add the insight for the different hours
# add the possible the weather in the next 3 days as well 
for key, val in api.canton_capital_dict.items():
    st.write(key, )