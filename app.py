import streamlit as st
from db_operations import *

st.title("🍽️ Restaurant Management System")

if "role" not in st.session_state:
    st.session_state.role = None
    st.session_state.user = None

# ---------------- LOGIN ----------------
phone = st.text_input("Phone")
password = st.text_input("Password", type="password")
role = st.radio("Login as", ["Admin", "Server", "Chef", "Customer"])

if st.button("Login"):
    if role == "Customer":
        user = customerLogin(phone, password)
    else:
        user = employeeLogin(phone, password)

    if user:
        st.session_state.role = role
        st.session_state.user = user
        st.success("Login successful")
    else:
        st.error("Invalid credentials")

# ---------------- ADMIN ----------------
if st.session_state.role == "Admin":
    st.header("Admin Panel")

    name = st.text_input("Employee Name")
    phone = st.text_input("Employee Phone")
    role_emp = st.selectbox("Role", ["Admin", "Server", "Chef"])
    pwd = st.text_input("Password", type="password")

    if st.button("Add Employee"):
        insertEmployee(name, phone, role_emp, pwd)
        st.success("Employee Added")

    st.subheader("Employees")
    st.table(fetchEmployees())

# ---------------- CUSTOMER ----------------
if st.session_state.role == "Customer":
    st.header("Pre-Order Food")

    menu = fetchMenu()
    item = st.selectbox("Item", menu, format_func=lambda x: x[1])
    qty = st.number_input("Quantity", 1)

    if st.button("Place Order"):
        oid = createOrder(st.session_state.user[0])
        addOrderItem(oid, item[0], qty)
        st.success("Order placed")

# ---------------- CHEF ----------------
if st.session_state.role == "Chef":
    st.header("Chef Dashboard")

    orders = fetchOrders()
    for o in orders:
        st.write(o)
        if st.button(f"Prepare Order {o[0]}"):
            reduceInventory(o[4], o[2])
            markPrepared(o[0])
            st.success("Prepared & inventory updated")
    total = generateBill(o[0])
    st.success(f"Order completed. Bill Amount: ₹{total}")
if st.session_state.role == "Admin":
    st.header("📊 Admin Dashboard")

    stats = adminStats()

    col1, col2 = st.columns(2)
    col1.metric("Employees", stats["employees"])
    col1.metric("Customers", stats["customers"])

    col2.metric("Orders", stats["orders"])
    col2.metric("Total Revenue (₹)", stats["revenue"])

    st.subheader("Daily Sales Report")
    st.table(getDailySales())
if st.session_state.role == "Customer":
    st.subheader("📜 My Order History")
    history = getCustomerOrderHistory(st.session_state.user[0])
    st.table(history)
