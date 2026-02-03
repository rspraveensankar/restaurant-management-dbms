#####################################################################
#####################################################################
####                                                             ####
####           Run Only Once To Create Restaurant Tables         ####
####                                                             ####
#####################################################################
#####################################################################

import sqlite3

conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

# -------------------- EMPLOYEE TABLE --------------------
def createTableEmployee():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT UNIQUE,
        gender TEXT,
        designation TEXT,
        salary INTEGER,
        dob DATE,
        address TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

# -------------------- CUSTOMER TABLE --------------------
def createTableCustomer():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT UNIQUE,
        gender TEXT,
        date_of_registration DATE DEFAULT CURRENT_DATE
    )
    """)

# -------------------- MENU TABLE --------------------
def createTableMenu():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT,
        availability TEXT CHECK(availability IN ('Yes','No')) DEFAULT 'Yes'
    )
    """)

# -------------------- ORDERS TABLE --------------------
def createTableOrders():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        employee_id INTEGER,
        order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        status TEXT CHECK(status IN ('Placed','Preparing','Served','Cancelled')) DEFAULT 'Placed',
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
    )
    """)

# -------------------- ORDER ITEMS TABLE --------------------
def createTableOrderItems():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        menu_id INTEGER,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (menu_id) REFERENCES menu(menu_id)
    )
    """)

# -------------------- INVENTORY TABLE --------------------
def createTableInventory():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        unit TEXT,
        last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

# -------------------- CREATE ALL TABLES --------------------

createTableEmployee()
createTableCustomer()
createTableMenu()
createTableOrders()
createTableOrderItems()
createTableInventory()

conn.commit()
conn.close()
