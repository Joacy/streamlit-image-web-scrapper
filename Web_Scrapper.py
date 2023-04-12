import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

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

if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, "lxml")
    rows = soup.find_all("div", class_="ripi6")
        
    col1, col2, col3, col4 = placeholder.columns(4)

    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(4):
            img = figures[i].find("img", class_="tB6UZ a5VGX")
            img_url = img["srcset"].split("?")[0]
            anchor = figures[i].find("a", class_="rEAWd")
            print(anchor["href"])

            if i == 0:
                col1.image(img_url)
                btn = col1.button("Donwload", key=str(index) + "_" + str(i))
                if btn:
                    print("Butão clicado")
                    webbrowser.open_new_tab(f"https://unsplash.com/{anchor['href']}")
            elif i == 1:
                col2.image(img_url)
                btn = col2.button("Donwload", key=str(index) + "_" + str(i))
                if btn:
                    webbrowser.open_new_tab(f"https://unsplash.com/{anchor['href']}")
            elif i == 2:
                col3.image(img_url)
                btn = col3.button("Donwload", key=str(index) + "_" + str(i))
                if btn:
                    webbrowser.open_new_tab(f"https://unsplash.com/{anchor['href']}")
            elif i == 3:
                col4.image(img_url)
                btn = col4.button("Donwload", key=str(index) + "_" + str(i))
                if btn:
                    webbrowser.open_new_tab(f"https://unsplash.com/{anchor['href']}")