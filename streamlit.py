import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Bank analysis')
st.text('Разведочный анализ данных банка')

data = pd.read_csv('combined.csv')

st.subheader('Гистограма распределения')

column_name = st.selectbox('Выберете признак',('TARGET','AGE','SOCSTATUS_WORK_FL','SOCSTATUS_PENS_FL','GENDER',
'CHILD_TOTAL','DEPENDANTS','PERSONAL_INCOME','LOAN_NUM_TOTAL','LOAN_NUM_CLOSED'))

if len(data[column_name].unique())>100:
    bins_hs = 100
else:
    bins_hs = len(data[column_name].unique())

fig, ax = plt.subplots()
ax.hist(data[column_name],bins = bins_hs)

st.pyplot(fig)
