import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(
  page_title="Web Scrapper",
  page_icon="",
  layout="wide"
)

st.markdown("<h1 style='text-align: center;'>Web Scrapper</h1>", unsafe_allow_html=True)

with st.form("Busca"):
    keyword = st.text_input("O que procura?")
    search = st.form_submit_button("Buscar Imagens")

placeholder = st.empty()

if search:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, "lxml")
    rows = soup.find_all("div", class_="ripi6")
        
    col1, col2, col3, col4 = placeholder.columns(4)
    
    for row in rows:
        figures = row.find_all("figure")
        for i in range(4):
            img = figures[i].find("img", class_="tB6UZ a5VGX")
            img_url = img["srcset"].split("?")[0]
            if i == 0:
                col1.image(img_url)
            elif i == 1:
                col2.image(img_url)
            elif i == 2:
                col3.image(img_url)
            elif i == 3:
                col4.image(img_url)

# div:ripi6=>figure=>img:tB6UZ a5VGX