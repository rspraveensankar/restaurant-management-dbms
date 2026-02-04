from db_operations import (
    insertEmployee,
    insertCustomer,
    insertMenu,
    insertInventory,
    createOrder,
    addOrderItem
)

# ================= EMPLOYEES =================
insertEmployee("Admin User", "9990001111", "Admin", "admin123")

insertEmployee("Ravi Kumar", "9990002222", "Server", "server123")
insertEmployee("Suresh", "9990004444", "Server", "server123")

insertEmployee("Kumar Chef", "9990003333", "Chef", "chef123")
insertEmployee("Manoj Chef", "9990005555", "Chef", "chef123")


# ================= CUSTOMERS =================
insertCustomer("Arun", "8881112222", "cust123")
insertCustomer("Priya", "8883334444", "cust123")
insertCustomer("Karthik", "8885556666", "cust123")
insertCustomer("Divya", "8887778888", "cust123")
insertCustomer("Sanjay", "8889990000", "cust123")


# ================= INVENTORY =================
insertInventory("Rice", 20000, "grams")
insertInventory("Chicken", 12000, "grams")
insertInventory("Oil", 8000, "ml")
insertInventory("Salt", 2000, "grams")
insertInventory("Spices", 1500, "grams")
insertInventory("Paneer", 4000, "grams")
insertInventory("Vegetables", 6000, "grams")
insertInventory("Butter", 3000, "grams")


# ================= MENU =================
insertMenu(
    "Chicken Biryani",
    180,
    "Rice:200,Chicken:150,Oil:20,Spices:5,Salt:2"
)

insertMenu(
    "Veg Fried Rice",
    120,
    "Rice:200,Vegetables:100,Oil:15,Spices:4,Salt:2"
)

insertMenu(
    "Chicken Fry",
    160,
    "Chicken:200,Oil:30,Spices:6,Salt:2"
)

insertMenu(
    "Paneer Butter Masala",
    170,
    "Paneer:150,Butter:20,Oil:15,Spices:6,Salt:2"
)

insertMenu(
    "Plain Rice",
    80,
    "Rice:250,Salt:2"
)

insertMenu(
    "Veg Curry",
    110,
    "Vegetables:150,Oil:15,Spices:5,Salt:2"
)


# ================= ORDERS + ORDER ITEMS =================
# Customer 1
order1 = createOrder(1)
addOrderItem(order1, 1, 2)   # Chicken Biryani x2
addOrderItem(order1, 3, 1)   # Chicken Fry x1

# Customer 2
order2 = createOrder(2)
addOrderItem(order2, 2, 1)   # Veg Fried Rice x1
addOrderItem(order2, 6, 1)   # Veg Curry x1

# Customer 3
order3 = createOrder(3)
addOrderItem(order3, 4, 1)   # Paneer Butter Masala x1
addOrderItem(order3, 5, 2)   # Plain Rice x2

# Customer 4
order4 = createOrder(4)
addOrderItem(order4, 1, 1)   # Chicken Biryani x1
addOrderItem(order4, 6, 1)   # Veg Curry x1

# Customer 5
order5 = createOrder(5)
addOrderItem(order5, 2, 2)   # Veg Fried Rice x2

print("✅ Extended sample data inserted successfully")
