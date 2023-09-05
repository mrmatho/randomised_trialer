from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
from collections import Counter

st.title("Randomised Trialer")
st.header("Randomly generate probability simulations", divider="rainbow")

with st.sidebar:
  
  opts_n = st.slider("Number of Options", min_value=2, max_value=10, value=2)
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
st.subheader("As a spinner")
st.altair_chart(pie, use_container_width=False, theme=None)

n = st.slider("Number of Simulations (n):", min_value=1, max_value=10000, value=50)
sampleNumbers = np.random.choice(opts_name, n, p=prob)
sampleVals = dict(Counter(sampleNumbers))
st.table(sampleVals)

st.subheader("Chart of values")
st.bar_chart(sampleVals)

st.write(sampleNumbers)
