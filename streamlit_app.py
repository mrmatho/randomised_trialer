from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st

import streamlit as st

st.title("Randomised Trialer")
st.header("Randomly generate your own simlations in probability", divider="rainbow")
opts_n = st.slider("Number of Options", min_value=2, max_value=10, value=2)
variable_prob = st.toggle('Use Variable Probabilities')

opts_name = []
opts_val = []

for i in range(1, opts_n + 1):
  opts_name.append(st.text_input(f"Option {i} Name:", value=f"Option {i}"))
  if variable_prob:
    opts_val.append(st.slider(f"How many for option {i}?", min_value=1, max_value=20, value=1))
  else:
    opts_val.append(1)

pie_source = pd.DataFrame({"category": opts_name, "value": opts_val})

pie = alt.Chart(pie_source).mark_arc().encode(
    theta="value",
    color="category"
)
st.header("As a spinner")
st.altair_chart(pie, use_container_width=False)

