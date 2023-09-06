from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
from collections import Counter


st.set_page_config(
    page_title="Randomised Trialer",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Mr Matheson's Randomised Trialer")
st.subheader("Randomly generate probability simulations", divider="rainbow")

with st.sidebar:
  st.header("Set up the Simulation")
  opts_n = st.slider("Number of Options", min_value=2, max_value=20, value=4)
  variable_prob = st.toggle('Use Variable Probabilities')
  
  opts_name = []
  opts_val = []

  total = 0
  for i in range(1, opts_n + 1):
    name = st.text_input(f"Option{i} Name:", value=f"Option{i}")
    opts_name.append(name)
    if variable_prob:
      n = st.slider(f"How many for {name}?", key=f"option{i}", min_value=1, max_value=20, value=1)
      opts_val.append(n)
      total += n
    else:
      opts_val.append(1)
      total += 1

  prob = [x / total for x in opts_val]
  pie_source = pd.DataFrame({"category": opts_name, "value": prob})


pie = alt.Chart(pie_source).mark_arc().encode(
    theta="value",
    color="category"
)
col1, col2 = st.columns(2)
with col1:
  st.subheader("Theoretical Probability")
  st.altair_chart(pie, use_container_width=True, theme=None)

with col2:
  # n = st.slider("Number of Simulations (n):", min_value=1, max_value=10000, value=50)
  n = st.number_input("Number of Simulations (1 - 10,000)", min_value=1, max_value=10000, value= 50)
  
sampleNumbers = np.random.choice(opts_name, n, p=prob)

sl = list(sampleNumbers)
counts = []
for name in opts_name:
  counts.append(sl.count(name))

sampleVals = pd.DataFrame( {
  "Selection": opts_name,
  "Frequency": counts, 
  "Theoretical Probability": prob
})  

st.subheader("Simulation Results")
col3, col4 = st.columns(2)
with col3:
  # Trying out a bar chart with tick marks from altair
  bar = alt.Chart(sampleVals).mark_bar().encode(
    x='Selection',
    y='Frequency'
)

tick = alt.Chart(sampleVals).mark_tick(
    color='red',
    thickness=2,
    size=40 * 0.9,  # controls width of tick.
).encode(
    x='Selection',
    y='Theoretical Probability'
)

c = bar + tick
st.altair_chart(c, use_container_width=True, theme=None)
  

with col4:
  st.subheader("Results Table")
  st.dataframe(sampleVals)
  st.subheader("Full set of results (in order)")
  st.write(sampleNumbers)
  
