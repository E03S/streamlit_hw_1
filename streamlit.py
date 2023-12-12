import streamlit as st
import pandas as pd
import numpy as np

st.title('Bank analysis')
st.text('Разведочный анализ данных банка')

data = pd.read_csv('combined.csv')

st.subheader('Гистограма распределения')

column_name = st.selectbox('Выберете признак',('AGREEMENT_RK','TARGET','AGE','SOCSTATUS_WORK_FL','SOCSTATUS_PENS_FL','GENDER',
'CHILD_TOTAL','DEPENDANTS','PERSONAL_INCOME','LOAN_NUM_TOTAL','LOAN_NUM_CLOSED'))

hist_values = np.histogram(
    data[column_name], bins=100)

st.bar_chart(hist_values)