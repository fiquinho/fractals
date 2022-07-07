import streamlit as st
import streamlit.components.v1 as components


st.markdown("# Fractal Tree")
st.markdown("Change the values of the variables:")
st.markdown(" - **DEPTH** = The number of layers")
st.markdown(" - **BRANCHES** = Number of branches on each level")
st.markdown(" - **ANGLE** = The angle between branches")
st.markdown(" - **DRAW_CHANCE** = The chance of every branch to get rendered")

components.iframe("https://replit.com/@FedericoBogado/FractalTree?lite=true", height=1000, width=1000)
