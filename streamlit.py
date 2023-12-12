import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Bank analysis')
st.text('Разведочный анализ данных банка')

data = pd.read_csv('combined.csv')

st.subheader('Гистограма распределения')

column_name = st.selectbox('Выберете признак',('TARGET','AGE','SOCSTATUS_WORK_FL','SOCSTATUS_PENS_FL','GENDER',
'CHILD_TOTAL','DEPENDANTS','PERSONAL_INCOME','LOAN_NUM_TOTAL','LOAN_NUM_CLOSED'),key = 1)

if len(data[column_name].unique())>100:
    bins_hs = 100
else:
    bins_hs = len(data[column_name].unique())

fig, ax = plt.subplots()
ax.hist(data[column_name],bins = bins_hs)

st.pyplot(fig)

st.subheader('Числовые характеристики')

column_name_2 = st.selectbox('Выберете признак',('AGE','SOCSTATUS_WORK_FL','SOCSTATUS_PENS_FL','GENDER',
'CHILD_TOTAL','DEPENDANTS','PERSONAL_INCOME','LOAN_NUM_TOTAL','LOAN_NUM_CLOSED'),key = 2)

st.dataframe(data[column_name_2].describe())

st.subheader('Матрица корреляции')

fig_2, ax_2 = plt.subplots()
clb = ax_2.matshow(data.corr())
fig_2.colorbar(clb)
plt.xticks(range(len(data.columns)),data.columns,rotation = 90)
plt.yticks(range(len(data.columns)),data.columns)

st.pyplot(fig_2)

st.subheader('Распределения признаков при разных целевых')

column_name_3 = st.selectbox('Выберете признак',('AGE','SOCSTATUS_WORK_FL','SOCSTATUS_PENS_FL','GENDER',
'CHILD_TOTAL','DEPENDANTS','PERSONAL_INCOME','LOAN_NUM_TOTAL','LOAN_NUM_CLOSED'),key = 3)

if len(data[column_name_3].unique())>100:
    bins_hs = 100
else:
    bins_hs = len(data[column_name_3].unique())

fig_3, ax_3 = plt.subplots(2)
ax_3[0].hist(data[data['TARGET']==1][column_name_3],bins = bins_hs)
ax_3[0].set_title('Целевая переменная 1')
ax_3[1].hist(data[data['TARGET']==0][column_name_3],bins = bins_hs)
ax_3[1].set_title('Целевая переменная 0')

st.pyplot(fig_3)