import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

l_col_1, r_col_1 = st.columns(2)

with r_col_1:
    st_lottie(
        load_lottie_file("4th_lottie_anime.json"),
        speed=3,
        reverse=True,
        loop=True,
        quality="high",
        height=200,
        width=None,
        key="anime",
    )
with l_col_2:
  st.write("there you go")


      
