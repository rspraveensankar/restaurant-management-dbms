import streamlit as st
from db_operations import fetchMenu, createOrder, addOrderItem, getCustomerOrderHistory

if st.session_state.get("role") != "Customer":
    st.switch_page("app.py")

st.title("🧑 Customer Portal")

menu = fetchMenu()
item = st.selectbox("Select Item", menu, format_func=lambda x: x[1])
qty = st.number_input("Quantity", 1)

if st.button("Pre-Order"):
    order_id = createOrder(st.session_state.user[0])
    addOrderItem(order_id, item[0], qty)
    st.success("Order placed successfully")

st.subheader("📜 Order History")
st.table(getCustomerOrderHistory(st.session_state.user[0]))

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
