from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st

import streamlit as st
opts_n = st.slider("Number of Options", min_value=2, max_value=10, value=2)
variable_prob = st.toggle('Use Variable Probabilities')

opts_name = []
opts_val = []

for i in range(1, opts_n + 1):
  opts_name.append(st.text_input("Option Name:"))
  
