import streamlit as st
import random


st.title("ProjectAstra")
slider = st.slider("Age", 0, 100)
st.write(f"Run ID: {random.randint(1, 100000)}")
user_msg=st.text_input("Chat",placeholder="Lets chat")
if (st.button("Send")):
    st.text("You entered:" + user_msg)

