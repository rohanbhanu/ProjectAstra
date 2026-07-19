import streamlit as st
import requests as req

st.title("Project Astra")

user_msg = st.text_input("Chat", placeholder="Let's chat")

if st.button("Send"):

    st.write(f"You entered: {user_msg}")

    resp = req.post(
        "http://127.0.0.1:8000/chat",
        json={
            "message": user_msg
        }
    )

    if resp.status_code == 200:
        data = resp.json()
        st.write(data["reply"])
    else:
        st.error("Backend request failed.")