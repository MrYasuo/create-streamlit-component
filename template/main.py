import streamlit as st
from my_component import my_component

component_name, component_value = my_component()
st.write(component_name)
