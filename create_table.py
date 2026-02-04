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

# ---------------- DROP TABLES (SAFE RESET) ----------------
cursor.execute("DROP TABLE IF EXISTS order_items")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS inventory")
cursor.execute("DROP TABLE IF EXISTS menu")
cursor.execute("DROP TABLE IF EXISTS customer")
cursor.execute("DROP TABLE IF EXISTS employee")
# ---------------- CREATE TABLES ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT UNIQUE,
    role TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu (
    menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    price REAL,
    ingredients TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT UNIQUE,
    quantity INTEGER,
    unit TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    status TEXT DEFAULT 'Placed'
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    menu_id INTEGER,
    quantity INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS billing (
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    total_amount REAL,
    bill_date DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS payment (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER,
    payment_mode TEXT,
    payment_status TEXT,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")


conn.commit()
conn.close()

print("✅ Tables created successfully")
