import streamlit as st
import pickle

st.title("creditcard.csv")
model=pickle.load(open('model.pkl','rb'))

col1,col2=st.columns(2)
time=col1.number_input('Enter time')
amount=col2.number_input('Enter amount')

if st.button('predict'):
    data=[[time,amount]]
    result=model.predict(data)[0]
    st.success(result)




