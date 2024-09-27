import streamlit as st
import os

st.write("""
Mon premier est une lettre de l'alphabet, souvent associée à une question ou à une incertitude.
Mon deuxième est un mot désignant un élément de la nature qui est essentiel à la vie, souvent associé à la transparence et à la fluidité.
Mon tout est un concept philosophique et mathématique, souvent considéré comme fondamental dans la logique et les sciences.
mon dernier ne peut etre stocké que sur 8 bits + 1""")

if st.text_input(label="enter the code") == os.environ["code"]:
  st.write("92006fa632c3777478a924d3f21cd9eb1a21e4164bdbfa90490c9e77c9ae22e0")
else:
  st.write("try other things !")
