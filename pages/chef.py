import streamlit as st
from db_operations import fetchOrders, reduceInventory, markPrepared, generateBill

if st.session_state.get("role") != "Chef":
    st.switch_page("app.py")

st.title("👨‍🍳 Chef Dashboard")

orders = fetchOrders()

for o in orders:
    st.write(f"Order {o[0]} | {o[1]} x{o[2]}")
    if st.button(f"Prepare Order {o[0]}"):
        reduceInventory(o[4], o[2])
        markPrepared(o[0])
        bill = generateBill(o[0])
        st.success(f"Prepared | Bill ₹{bill}")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
