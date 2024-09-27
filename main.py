import streamlit as st
import os

st.write("""
Je suis là, mais je ne suis pas visible, je peux être calculé mais jamais touché, dans les ombres de la mémoire, je garde un secret. Que suis-je ?
mon dernier ne peut etre stocké que sur 8 bits + 1""")

if st.text_input(label="enter the code") == os.environ["code"]:
  st.write("92006fa632c3777478a924d3f21cd9eb1a21e4164bdbfa90490c9e77c9ae22e0")
else:
  st.write("try other things !")
