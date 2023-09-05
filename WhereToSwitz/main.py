import streamlit as st
from PIL import Image
import api

map = Image.open(r"C:\Users\48694\Desktop\CSstudies\PersonalProjects\WhereToSwitz\SwitzCantons.jpg")

st.title('WhereToSwitz - Where is a good weather in Switzerland!')
st.subheader('Map of Switzerland Cantons')

st.image(map)



tab1, tab2, tab3 = st.tabs(["Sun", "Clouds", "Rain"])
    
with tab1:
   st.header("Sun")
   st.write(api.canton_capital_dict['Aargau']['temp'],
            api.canton_capital_dict['Aargau']['weather'],
            api.canton_capital_dict['Aargau']['distinct_weather'],
            st.image(api.icon_data))
   

with tab2:
   st.header("Clouds")

with tab3:
   st.header("Rain/Snow")





# for key, val in api.canton_capital_dict.items():
#     st.write(key, val)

# TO DO
# catch the data to not to call them every time
# add the insight for the different hours
# add the possible the weather in the next 3 days as well 
# You can add functionality to look for a specyfic cities 
