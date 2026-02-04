import streamlit as st
from db_operations import createOrder

if st.session_state.get("role") != "Server":
    st.switch_page("app.py")

st.title("🧾 Server Dashboard")

customer_id = st.number_input("Customer ID", min_value=1)

if st.button("Create Order"):
    oid = createOrder(customer_id)
    st.success(f"Order {oid} created")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
