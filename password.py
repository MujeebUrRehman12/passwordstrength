import streamlit as st
import re

#page styling

st.set_page_config(page_title="Password Strength", layout="centered")

#custum css

st.markdown(
    """"
    <style>
    .main {
        text-align: center;
    }
    .stTextInput {
        width: 60% !important;
    }
    .stButton button {
        width: 50%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
    }
    stButton button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#page title
st.title("Password Strength Checker")
st.write("Enter a password to check its strength:")

#function to check password strength

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    #display password strength result
    if score == 4:
        st.success("Password is strong!")
    elif score == 3:
        st.warning("Password is medium.")
    else:
        st.error("Password is weak.")

    #display password strength feedback
    if feedback:
        with st.expander("Improved Your Password"):
            for item in feedback:
                st.write(item)
password = st.text_input("Password", type="password")      

#button working 
if st.button("Check Password"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password.")