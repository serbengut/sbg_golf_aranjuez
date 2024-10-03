import streamlit as st
import pandas as pd 
#from db_fxns import * 
import streamlit.components.v1 as stc



# Data Viz Pkgs
import plotly.express as px 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

st.set_page_config(
     page_title = 'Golf Aranjuez',
     #page_icon = 'heart.jpg',
     layout = 'wide')

st.title(':green[Golf Aranjuez]')

st.success('Hoyo 1')
st.selectbox('Golpes',[0,1,2,3,4,5,6,7,8,9])
st.selectbox('Salida',['Recto', 'Dcha', 'Izq'])
