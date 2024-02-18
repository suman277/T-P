import streamlit as st
num1=st.number_input("Enter the number")
num2=st.number_input("Enter the NUmber 2")
if st.button("add"):
    st.write(f"# {num1+num2}")
st.file_uploader("Upolad a csv")
