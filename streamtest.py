import streamlit as st

import datetime

from f1 import test as z

from PIL import Image as i

import pandas as pd
import numpy as np

st.title('Welcome to streamlit')

st.header('I am a header')

st.subheader(' I am a subheader')

st.markdown("**Streamlit** is a widely used GUI for machine learning apps")
html_string = "<h3>this is an html string</h3>"

st.markdown("<h3><u>this is an html string</u></h3>", unsafe_allow_html=True)

st.success("this is success")

st.info('normal info')

st.warning('be laert')

st.error('its error ')

x=ZeroDivisionError('divide by 0')
st.exception(x)

st.write('WELCOME ALL')

#p=i.open('C:\\streamlitdemo\\winter.jpg')
p=i.open('winter.jpg')


st.image(p,width=300)

if st.checkbox('show/hide'):
    st.text('showing the data')


status=st.radio('select gender: ',('female','male'))
                

if status=='female':
    st.success('FEMALE')
else:
    st.success('Male')

hobby=st.selectbox('Hobbies',['Movie','Football','songs'])

st.write("my hobbey is "+hobby)


h=st.multiselect('Hobbies',['Movie','Football','songs','travelling','politics'])

st.write("my hobbeies  are ",len(h))

st.button('I am a button')

if st.button('click me'):
    st.text('welcome..........')

name=st.text_input('enter name here','type here!!!!')

if st.button('submit'):
    st.text('the name is '+z(name))


level=st.slider('select the level',1,20)
st.text('selected: {}'.format(level))


lang=st.radio('what language U like?',('c','c++','java','python'))

if lang=='c':
    st.write('U selected C')
elif lang=='c++':
    st.write('U selected C++')
elif lang=='java':
    st.write('U selected JAVA')
else:
    st.write('U selected Python')

age=st.slider('please enter age',min_value=0,max_value=100,value=10)
st.write('age is ',age)

d=st.date_input('Whats your Birthday',datetime.date(2020,1,1),datetime.date(1990,1,1),datetime.datetime.now())
st.write('bday is ',d)

ch=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])



st.line_chart(ch)

st.bar_chart(ch)

st.area_chart(ch)

















