import streamlit as st
from PIL import Image
import api
import pandas as pd
import numpy as np
import random

map = Image.open(r"C:\Users\48694\Desktop\CSstudies\PersonalProjects\WhereToSwitz\SwitzCantons.jpg")

st.title('WhereToSwitz - Where is a good weather in Switzerland!')
st.subheader('Map of Switzerland Cantons')

st.image(map)



tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Sun", "Clouds", "Rain"])

with tab1:
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


with tab2:
   st.header("Sun")
   # 20/
   

with tab3:
   st.header("Clouds")

with tab4:
   st.header("Rain/Snow")





# for key, val in api.canton_capital_dict.items():
#     st.write(key, val)

# TO DO
# catch the data to not to call them every time
# add the insight for the different hours
# add the possible the weather in the next 3 days as well 
# You can add functionality to look for a specyfic cities 
