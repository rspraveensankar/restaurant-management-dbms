import streamlit as st
from db_operations import (
    insertEmployee,
    fetchAllEmployees,
    insertCustomer,
    fetchAllCustomers,
    insertMenuItem,
    fetchMenu
)

st.title("🍽️ Restaurant Management System")

menu = st.sidebar.selectbox(
    "Select Module",
    ["Employee", "Customer", "Menu"]
)

if menu == "Employee":
    st.subheader("Add Employee")
    
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    gender = st.selectbox("Gender", ["Male", "Female"])
    designation = st.text_input("Designation")
    salary = st.number_input("Salary", 0)
    dob = st.date_input("Date of Birth")
    address = st.text_area("Address")

    if st.button("Add Employee"):
        insertEmployee(name, phone, gender, designation, salary, dob, address)
        st.success("Employee added successfully!")

    st.subheader("Employee List")
    st.table(fetchAllEmployees())
