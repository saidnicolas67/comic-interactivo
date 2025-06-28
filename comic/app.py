
import streamlit as st
import os

st.set_page_config(page_title="Cómic de AFOPY", layout="centered")
st.title("🌱 La historia de una lechuga feliz")

comic_folder = "comic"
pages = sorted([img for img in os.listdir(comic_folder) if img.endswith(('.png', '.jpg'))])

if "page" not in st.session_state:
    st.session_state.page = 0

img_path = os.path.join(comic_folder, pages[st.session_state.page])
st.image(img_path, use_container_width=True)

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️ Anterior", disabled=st.session_state.page == 0):
        st.session_state.page -= 1

with col3:
    if st.button("Siguiente ➡️", disabled=st.session_state.page == len(pages)-1):
        st.session_state.page += 1
