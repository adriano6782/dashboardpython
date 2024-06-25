import streamlit as st  
import pandas as pd
import plotly.express as px 

# Corrigido o nome do arquivo para incluir a extensão .csv
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
