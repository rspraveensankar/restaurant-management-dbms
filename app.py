import streamlit as st
from db_operations import employeeLogin, customerLogin

st.set_page_config(page_title="Restaurant Management System", layout="centered")

st.title("🍽️ Restaurant Management System")

# Reset on first load
if "role" not in st.session_state:
    st.session_state.clear()

phone = st.text_input("Phone")
password = st.text_input("Password", type="password")
role = st.radio("Login as", ["Admin", "Server", "Chef", "Customer"])

if st.button("Login"):
    if role == "Customer":
        user = customerLogin(phone, password)
    else:
        user = employeeLogin(phone, password)

    if user:
        st.session_state.user = user
        st.session_state.role = role

        # 🚀 INDUSTRY-STYLE REDIRECT
        if role == "Admin":
            st.switch_page("pages/admin.py")
        elif role == "Server":
            st.switch_page("pages/server.py")
        elif role == "Chef":
            st.switch_page("pages/chef.py")
        elif role == "Customer":
            st.switch_page("pages/customer.py")
    else:
        st.error("Invalid credentials")
