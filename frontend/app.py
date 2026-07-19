import streamlit as st
import requests as req
from config import BACKEND_URL
st.title("Project Astra")

user_msg = st.text_input("Chat", placeholder="Let's chat")
if "ReqResJSON" not in st.session_state:
    st.session_state["ReqResJSON"]=[]


if st.button("Send"):


    resp = req.post(
        f"{BACKEND_URL}/chat",
        json={
            "message": user_msg
        }
    )
    st.session_state["ReqResJSON"].append(
            {
                "role":"User",
                "content":user_msg
            }
        )

    if resp.status_code == 200:
        data = resp.json()
        st.session_state["ReqResJSON"].append(
            {
                "role":"assistant",
                "content":data["reply"]
            }
        )

        for msg in st.session_state["ReqResJSON"]:
            st.write(f"{msg['role'].title()}: {msg['content']}")
            
    else:
        st.error("Backend request failed.")