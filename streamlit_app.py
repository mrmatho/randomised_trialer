from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
from collections import Counter

#st.title("Randomised Trialer")
st.header("Randomly generate probability simulations", divider="rainbow")

with st.sidebar:
  
  opts_n = st.slider("Number of Options", min_value=2, max_value=10, value=3)
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
st.write(len(sampleNumbers))
sampleVals = dict(Counter(sampleNumbers))
  

st.subheader("Simulation Results")
col3, col4 = st.columns(2)
with col3:
  st.bar_chart(sampleVals)

with col4:
  st.subheading("Results Table")
  st.table(sampleVals)
  st.subheading("Full set of results (in order)")
  st.write(sampleNumbers)
  
