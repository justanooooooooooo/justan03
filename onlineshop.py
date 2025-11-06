import streamlit as st

st.title("🛍️ Simple Online Store")

# --- 商品清單 ---
st.session_state.products = {
    # 🥦 Food & Drinks
    "Apple": 30,
    "Banana": 20,
    "Instant Noodles": 45,
    "Mineral Water": 25,
    "Chocolate": 60,
    "Bread": 35,
    "Tea Egg": 15,
    "Coffee": 55,
    "Cookies": 40,
    "Milk": 50,

    # 🧴 Daily Essentials
    "Toothbrush": 25,
    "Toothpaste": 60,
    "Shampoo": 120,
    "Body Wash": 110,
    "Tissue": 45,
    "Laundry Detergent": 180,
    "Trash Bag": 50,
    "Hand Sanitizer": 75,
    "Soap Bar": 90,
    "Hand Wash": 80,

    # 💻 Tech Accessories
    "Power Bank": 450,
    "Charging Cable": 120,
    "Bluetooth Earbuds": 850,
    "Mouse": 390,
    "Keyboard": 890,
    "USB Drive": 250,
    "Phone Holder": 150,
    "Type-C Adapter": 100,
    "Laptop Cooler": 680,
    "Screen Cleaner": 200,

    # 🎁 Stationery & Small Gifts
    "Pen": 25,
    "Notebook": 60,
    "Planner": 120,
    "Night Light": 180,
    "Coin Purse": 90,
    "Keychain": 70,
    "Water Bottle": 150,
    "Bookmark": 20,
    "Tape": 30,
    "Sticker Pack": 40
}

# 初始化購物車
if "cart" not in st.session_state:
    st.session_state.cart = {}

st.header("🛒 Product List")

# --- 顯示商品 ---
product_names = list(st.session_state.products.keys())
for i in range(0, len(product_names), 3):
    cols = st.columns(3)
    for j, name in enumerate(product_names[i:i+3]):
        with cols[j]:
            st.subheader(name)
            st.write(f"Price: {st.session_state.products[name]} NT$")
            qty = st.number_input("Quantity", min_value=0, value=0, key=f"{name}_qty")
            if st.button("Add to Cart", key=f"add_{name}"):
                if qty > 0:
                    if name in st.session_state.cart:
                        st.session_state.cart[name] += qty
                    else:
                        st.session_state.cart[name] = qty
                    st.success(f"Added {qty} x {name} to cart")

# --- 購物車區 ---
st.header("🧺 Shopping Cart")
if st.session_state.cart:
    total = 0
    for item, qty in st.session_state.cart.items():
        price = st.session_state.products[item] * qty
        st.write(f"{item} x {qty} = {price} NT$")
        total += price
    st.write(f"**Total: {total} NT$**")
    if st.button("Clear Cart"):
        st.session_state.cart = {}
        st.success("Cart cleared!")
else:
    st.write("Your cart is empty.")
