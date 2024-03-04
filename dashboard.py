import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
from io import StringIO

# Mengunduh data dari URL CSV
url_csv = "https://raw.githubusercontent.com/wahyuardiantito/Proyek_analisis_data/main/dataset/all_data.csv"
response_csv = requests.get(url_csv)
csv_data = StringIO(response_csv.text)

# Load data
all_df = pd.read_csv(csv_data)

# Pertanyaan Bisnis 1: Visualisasi rataan nilai pm2.5 untuk tiap jamnya
pm25_hourly = all_df.groupby('hour')['PM25'].mean()

# Pertanyaan Bisnis 2: Visualisasi pm2.5 tiap stasiun
pm25_station = all_df.groupby('station')['PM25'].mean()

#Pertanyaan Bisnis 3: Visualisasi intensitas curah hujan tiap stasiun
rainy_station = all_df.groupby('station')['RAIN'].mean()


# Streamlit Dashboard
st.title('Dashboard Kualitas Udara Sederhana')
st.sidebar.title('Pilih Visualisasi')

visualization_option = st.sidebar.selectbox(
    'Pilih Visualisasi yang Ingin Dilihat',
    ('Rata-rata nilai pm2.5 per jam', 'Rata-rata pm2.5 tiap stasiun', 'Intensitas hujan tiap stasiun')
)

if visualization_option == 'Rata-rata nilai pm2.5 per jam':
    st.subheader('Rata-rata nilai pm2.5 per jam')
    st.write(pm25_hourly)
    st.bar_chart(pm25_hourly)

elif visualization_option == 'Rata-rata pm2.5 tiap stasiun':
    st.subheader('Rata-rata pm2.5 tiap stasiun')
    st.write(pm25_station)
    st.bar_chart(pm25_station)

elif visualization_option == 'Intensitas hujan tiap stasiun':
    st.subheader('Intensitas hujan tiap stasiun')
    st.write(rainy_station)
    st.bar_chart(rainy_station)
