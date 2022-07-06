import multiprocessing

import streamlit as st
from fractal_tree import draw_fractal_tree


st.markdown("# Fractal Tree")
branches = st.number_input("Branches", value=4)
angle = st.number_input("Angle", value=30)
depth = st.number_input("Depth", value=5)
clicked = st.button("Paint")

t = multiprocessing.Process(target=draw_fractal_tree,
                            args=(branches, angle, depth,))

if clicked:
    t.start()
