import streamlit as st
import pandas as pd
import plotly.express as px

data1 = {
    'Jobs': ['Computer Systems Analysts',
'Network & Computer Systems Administrators',
'Computer Programmers',
'Software Developers',
'Software Quality Assurance Analysts & Testers',
'Web Developers',
'Web & Digital Interface Designers'],
'Hourly pay': [40.40,
34.50,
36.40,
46.74,
42.93,
33.07,
33.75],
}
data2 = {
    'Jobs': ['Computer Systems Analysts',
'Network & Computer Systems Administrators',
'Computer Programmers',
'Software Developers',
'Software Quality Assurance Analysts & Testers',
'Web Developers',
'Web & Digital Interface Designers'],
'Median Annual pay': [76900,
70720,
76170,
95020,
93900,
75240,
75120],
}
data3 = {
    'Jobs': ['Computer Systems Analysts',
'Computer Programmers',
'Computer User Support Specialists',
'Computer, ATM & Office Machine Repairers',
'Software Developers',
'Network & Computer Systems Administrators'],
'Entry Level Annual': [58930,
56730,
38560,
24660,
59320,
60820],
}
data4 = {
    'Jobs': ['Computer Systems Analysts',
'Computer Programmers',
'Computer User Support Specialists',
'Computer, ATM & Office Machine Repairers',
'Software Developers',
'Network & Computer Systems Administrators'],
'Expert Level Annual': [95420,
106150,
68960,
61600,
112700,
132450],
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)


st.title('Da Streamlit Graphs for Senior Greco')


fig1 = px.bar(df1, x='Jobs', y='Hourly pay', title=f'Job Hourly Pay')
st.plotly_chart(fig1)
fig2 = px.pie(df2, values='Median Annual pay', names='Jobs', title='Median Annual pay')
st.plotly_chart(fig2)
fig3 = px.bar(df3, x='Jobs', y='Entry Level Annual', title=f'Entry Level Annual')
st.plotly_chart(fig3)
fig4 = px.pie(df4, values='Expert Level Annual', names='Jobs', title='Expert Level Annual pay')
st.plotly_chart(fig4)