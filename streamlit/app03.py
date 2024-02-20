import streamlit as st

h = st.header('My Web Site')
s = st.subheader('เว็บไซต์ส่วนตัวของฉัน')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงื่อ')
banner = st.lmage('https://img.pikbest.com/backgrounds/20190330/')
b = st.button('click me')
text = st.text_input('prompt: ')
if text:
    st.image('http://4.bp.blogspot.com/-qDjXsrwZMao/T9gkC_P0c0I/')
    b = st.button('จะไปต่อหรือ...')
