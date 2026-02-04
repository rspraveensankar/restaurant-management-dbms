import sqlite3
import bcrypt

conn = sqlite3.connect("restaurant.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------- PASSWORD ----------------
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# ---------------- LOGIN ----------------
def employeeLogin(phone, password):
    cursor.execute("SELECT * FROM employee WHERE phone = ?", (phone,))
    user = cursor.fetchone()
    if user and verify_password(password, user[4]):
        return user
    return None

def customerLogin(phone, password):
    cursor.execute("SELECT * FROM customer WHERE phone = ?", (phone,))
    user = cursor.fetchone()
    if user and verify_password(password, user[3]):
        return user
    return None

# ---------------- EMPLOYEE ----------------
def insertEmployee(name, phone, role, password):
    cursor.execute("""
        INSERT INTO employee (name, phone, role, password)
        VALUES (?, ?, ?, ?)
    """, (name, phone, role, hash_password(password)))
    conn.commit()

def fetchEmployees():
    cursor.execute("SELECT employee_id, name, phone, role FROM employee")
    return cursor.fetchall()

def deleteEmployee(emp_id):
    cursor.execute("DELETE FROM employee WHERE employee_id = ?", (emp_id,))
    conn.commit()

# ---------------- CUSTOMER ----------------
def insertCustomer(name, phone, password):
    cursor.execute("""
        INSERT INTO customer (name, phone, password)
        VALUES (?, ?, ?)
    """, (name, phone, hash_password(password)))
    conn.commit()

# ---------------- MENU ----------------
def insertMenu(item, price, ingredients):
    cursor.execute("""
        INSERT INTO menu (item_name, price, ingredients)
        VALUES (?, ?, ?)
    """, (item, price, ingredients))
    conn.commit()

def fetchMenu():
    cursor.execute("SELECT * FROM menu")
    return cursor.fetchall()

# ---------------- INVENTORY ----------------
def insertInventory(name, qty, unit):
    cursor.execute("""
        INSERT OR IGNORE INTO inventory (ingredient_name, quantity, unit)
        VALUES (?, ?, ?)
    """, (name, qty, unit))
    conn.commit()

def reduceInventory(menu_id, qty):
    cursor.execute("SELECT ingredients FROM menu WHERE menu_id = ?", (menu_id,))
    ingredients = cursor.fetchone()[0]

    for i in ingredients.split(","):
        ing, used = i.split(":")
        cursor.execute("""
            UPDATE inventory
            SET quantity = quantity - (? * ?)
            WHERE ingredient_name = ?
        """, (int(used), qty, ing.strip()))
    conn.commit()

# ---------------- ORDER ----------------
def createOrder(customer_id):
    cursor.execute("INSERT INTO orders (customer_id) VALUES (?)", (customer_id,))
    conn.commit()
    return cursor.lastrowid

def addOrderItem(order_id, menu_id, qty):
    cursor.execute("""
        INSERT INTO order_items (order_id, menu_id, quantity)
        VALUES (?, ?, ?)
    """, (order_id, menu_id, qty))
    conn.commit()

def fetchOrders():
    cursor.execute("""
        SELECT o.order_id, m.item_name, oi.quantity, o.status, oi.menu_id
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN menu m ON oi.menu_id = m.menu_id
        WHERE o.status = 'Placed'
    """)
    return cursor.fetchall()

def markPrepared(order_id):
    cursor.execute("UPDATE orders SET status='Prepared' WHERE order_id=?", (order_id,))
    conn.commit()

# ---------------- BILLING ----------------
def generateBill(order_id):
    cursor.execute("""
        SELECT SUM(oi.quantity * m.price)
        FROM order_items oi
        JOIN menu m ON oi.menu_id = m.menu_id
        WHERE oi.order_id = ?
    """, (order_id,))
    
    total = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO billing (order_id, total_amount)
        VALUES (?, ?)
    """, (order_id, total))

    conn.commit()
    return total


def makePayment(bill_id, mode):
    cursor.execute("""
        INSERT INTO payment (bill_id, payment_mode, payment_status)
        VALUES (?, ?, 'Paid')
    """, (bill_id, mode))
    conn.commit()

def getDailySales():
    cursor.execute("""
        SELECT DATE(bill_date) AS date,
               SUM(total_amount) AS total_sales,
               COUNT(*) AS total_orders
        FROM billing
        GROUP BY DATE(bill_date)
        ORDER BY date DESC
    """)
    return cursor.fetchall()
def getCustomerOrderHistory(customer_id):
    cursor.execute("""
        SELECT o.order_id, o.status, b.total_amount, b.bill_date
        FROM orders o
        JOIN billing b ON o.order_id = b.order_id
        WHERE o.customer_id = ?
        ORDER BY b.bill_date DESC
    """, (customer_id,))
    
    return cursor.fetchall()
def adminStats():
    cursor.execute("SELECT COUNT(*) FROM employee")
    employees = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM customer")
    customers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM orders")
    orders = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(total_amount) FROM billing")
    revenue = cursor.fetchone()[0] or 0

    return {
        "employees": employees,
        "customers": customers,
        "orders": orders,
        "revenue": revenue
    }

def close_connection():
    conn.close()