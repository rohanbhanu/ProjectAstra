import streamlit as st
import requests as req
from config import BACKEND_URL

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Project Astra",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------------------------
# CSS
# ----------------------------------------------------
st.markdown("""
<style>

.user-row{
    display:flex;
    justify-content:flex-end;
    margin:12px 0;
}

.assistant-row{
    display:flex;
    justify-content:flex-start;
    margin:12px 0;
}

.user-bubble{
    background:#2b313e;
    color:white;
    padding:12px 18px;
    border-radius:18px;
    max-width:70%;
    font-size:16px;
}

.assistant-bubble{
    background:#f0f2f6;
    color:black;
    padding:12px 18px;
    border-radius:18px;
    max-width:70%;
    font-size:16px;
}

.avatar{
    font-size:28px;
    margin:0 10px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Title
# ----------------------------------------------------
st.title("🤖 Project Astra")
st.caption("Your Personal AI Assistant")

# ----------------------------------------------------
# Session State
# ----------------------------------------------------
if "ReqResJSON" not in st.session_state:
    st.session_state["ReqResJSON"] = []
if "waiting_for_reply" not in st.session_state:
    st.session_state["waiting_for_reply"] = False

if "pending_message" not in st.session_state:
    st.session_state["pending_message"] = ""
# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------
with st.sidebar:

    st.header("Project Astra")

    if st.button("🗑 Clear Chat"):
        st.session_state["ReqResJSON"] = []
        st.rerun()

# ----------------------------------------------------
# Display Chat History
# ----------------------------------------------------
for msg in st.session_state["ReqResJSON"]:

    if msg["role"] == "user":

        st.markdown(
            f"""
            <div class="user-row">
                <div class="user-bubble">
                    {msg["content"]}
                </div>
                <div class="avatar">👤</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            f"""
            <div class="assistant-row">
                <div class="avatar">🤖</div>
                <div class="assistant-bubble">
                    {msg["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ----------------------------------------------------
# Chat Input
# ----------------------------------------------------
user_msg = st.chat_input("Ask me anything...")

# ----------------------------------------------------
# Process New Message
# ----------------------------------------------------

if user_msg:

    # Save user message
    st.session_state["ReqResJSON"].append(
        {
            "role": "user",
            "content": user_msg
        }
        )
    st.session_state["pending_message"] = user_msg
    st.session_state["waiting_for_reply"] = True
    st.rerun()


if st.session_state["waiting_for_reply"] == True:
    try:
        with st.spinner("🤖 Astra is thinking..."):
            resp = req.post(
                f"{BACKEND_URL}/chat",
                json={
                    "message": st.session_state["pending_message"]
                },
                timeout=120
            )
        if resp.status_code == 200:
            data = resp.json()
            st.session_state["ReqResJSON"].append(
                {
                    "role": "assistant",
                    "content": data["reply"]
                }
            )
        else:
            st.session_state["ReqResJSON"].append(
                {
                    "role": "assistant",
                    "content": "⚠️ Backend request failed."
                }
            )
    except Exception as e:
        st.session_state["ReqResJSON"].append(
            {
                "role": "assistant",
                "content": f"⚠️ Error: {str(e)}"
            }
        )
    # Refresh page to show updated history
    st.session_state["waiting_for_reply"] = False
    st.session_state["pending_message"] = ""
    st.rerun()