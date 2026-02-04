import streamlit as st
from db_operations import adminStats, fetchEmployees, getDailySales

# 🔐 AUTH GUARD
if st.session_state.get("role") != "Admin":
    st.switch_page("app.py")

st.title("📊 Admin Dashboard")

stats = adminStats()

st.metric("Employees", stats["employees"])
st.metric("Customers", stats["customers"])
st.metric("Orders", stats["orders"])
st.metric("Revenue (₹)", stats["revenue"])

st.subheader("📅 Daily Sales")
st.table(getDailySales())

st.subheader("👨‍🍳 Employees")
st.table(fetchEmployees())

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
