import sqlite3

conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

def insertEmployee(name, phone, gender, designation, salary, dob, address):
    cursor.execute("""
        INSERT INTO employee 
        (name, phone, gender, designation, salary, dob, address)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, phone, gender, designation, salary, dob, address))
    conn.commit()


def fetchAllEmployees():
    cursor.execute("SELECT * FROM employee")
    return cursor.fetchall()


def updateEmployee(employee_id, salary, designation):
    cursor.execute("""
        UPDATE employee
        SET salary = ?, designation = ?
        WHERE employee_id = ?
    """, (salary, designation, employee_id))
    conn.commit()


def deleteEmployee(employee_id):
    cursor.execute(
        "DELETE FROM employee WHERE employee_id = ?",
        (employee_id,)
    )
    conn.commit()


def insertCustomer(name, phone, gender):
    cursor.execute("""
        INSERT INTO customer (name, phone, gender)
        VALUES (?, ?, ?)
    """, (name, phone, gender))
    conn.commit()


def fetchAllCustomers():
    cursor.execute("SELECT * FROM customer")
    return cursor.fetchall()


def deleteCustomer(customer_id):
    cursor.execute(
        "DELETE FROM customer WHERE customer_id = ?",
        (customer_id,)
    )
    conn.commit()

def insertMenuItem(item_name, price, category, availability="Yes"):
    cursor.execute("""
        INSERT INTO menu (item_name, price, category, availability)
        VALUES (?, ?, ?, ?)
    """, (item_name, price, category, availability))
    conn.commit()


def fetchMenu():
    cursor.execute("SELECT * FROM menu")
    return cursor.fetchall()


def updateMenuPrice(menu_id, price):
    cursor.execute("""
        UPDATE menu
        SET price = ?
        WHERE menu_id = ?
    """, (price, menu_id))
    conn.commit()


def deleteMenuItem(menu_id):
    cursor.execute(
        "DELETE FROM menu WHERE menu_id = ?",
        (menu_id,)
    )
    conn.commit()

def insertInventoryItem(ingredient_name, quantity, unit):
    cursor.execute("""
        INSERT INTO inventory (ingredient_name, quantity, unit)
        VALUES (?, ?, ?)
    """, (ingredient_name, quantity, unit))
    conn.commit()


def fetchInventory():
    cursor.execute("SELECT * FROM inventory")
    return cursor.fetchall()


def updateInventory(ingredient_id, quantity):
    cursor.execute("""
        UPDATE inventory
        SET quantity = ?
        WHERE ingredient_id = ?
    """, (quantity, ingredient_id))
    conn.commit()

def closeConnection():
    conn.close()