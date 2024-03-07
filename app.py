import streamlit as st

# Dictionary to store email-password pairs
credentials = {
    "FE23AI001@gmail.com": "12345",
    "FW23AI001@gmail.com": "12345",
    "FE23AI002@gmail.com": "12345",
    "FS23AI001@gmail.com": "12345"
}

def authenticate(email, password):
    # Check if email exists in the dictionary
    if email in credentials:
        # Check if the password matches
        if credentials[email] == password:
            return True
    return False

email = st.text_input('Enter email - ')
password = st.text_input('Enter Password - ', type='password')
btn = st.button('Login')

if btn:
    if authenticate(email, password):
        st.balloons()
        st.success("Logged In ")
    else:
        st.error('Login Failed')
