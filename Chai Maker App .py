import streamlit as st
import pandas as pd
from datetime import datetime
import uuid
import os

# =========================
# CONFIG
# =========================
st.set_page_config("Chai Maker Pro ☕", "🍵", layout="wide")

# =========================
# DATA
# =========================
chai_prices = {
    "Masala Chai": 30,
    "Ginger Chai": 15,
    "Cardamom Chai": 20,
    "Tulsi Chai": 10
}

if "cart" not in st.session_state:
    st.session_state.cart = []

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📊 Chai Dashboard")
st.sidebar.metric("Items in Cart", len(st.session_state.cart))
st.sidebar.write("☕ Chai Maker & Billing System")

# =========================
# HEADER
# =========================
st.title("🍵 Chai Maker Pro – Smart Billing System")
st.caption("Order • Customize • Bill • Save")

st.divider()

# =========================
# ORDER SECTION
# =========================
st.header("1️⃣ Customize Your Chai")

col1, col2 = st.columns(2)

with col1:
    chai_type = st.selectbox("Chai Type", chai_prices.keys())
    milk = st.selectbox("Milk Type", ["Whole", "Skim", "Almond", "Oat"])
    sugar = st.slider("Sugar (tsp)", 0, 5, 2)
    water = st.slider("Water Level", 0, 5, 3)
    qty = st.number_input("Cups", 1, 20, 1)

with col2:
    st.subheader("☕ Current Selection")
    st.write("Chai:", chai_type)
    st.write("Milk:", milk)
    st.write("Sugar:", sugar)
    st.write("Water:", water)
    st.write("Unit Price: ₹", chai_prices[chai_type])

if st.button("➕ Add to Cart"):
    item_total = qty * chai_prices[chai_type]
    st.session_state.cart.append(
        [chai_type, qty, chai_prices[chai_type], item_total]
    )
    st.success("Added to cart!")

# =========================
# CART SECTION
# =========================
st.divider()
st.header("2️⃣ Cart & Billing")

if st.session_state.cart:
    df = pd.DataFrame(
        st.session_state.cart,
        columns=["Item", "Qty", "Price", "Total"]
    )

    st.dataframe(df, use_container_width=True)

    subtotal = df["Total"].sum()
    tax = subtotal * 0.18
    discount = st.number_input("Discount ₹", 0.0, float(subtotal))
    grand_total = subtotal + tax - discount

    st.info(f"Subtotal: ₹{subtotal:.2f}")
    st.warning(f"Tax (18%): ₹{tax:.2f}")
    st.success(f"Grand Total: ₹{grand_total:.2f}")

else:
    st.warning("Cart is empty.")

# =========================
# CUSTOMER SECTION
# =========================
st.divider()
st.header("3️⃣ Customer & Payment")

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
payment = st.number_input("Amount Paid ₹", 0.0)

if payment:
    due = grand_total - payment
    st.metric("Amount Due", f"₹{due:.2f}")

# =========================
# SAVE INVOICE
# =========================
if st.button("✅ Confirm & Generate Invoice"):

    if not name:
        st.error("Enter customer name")
    elif not st.session_state.cart:
        st.error("Cart empty")
    else:
        invoice_id = str(uuid.uuid4())[:8]
        date = datetime.now().strftime("%d-%m-%Y %H:%M")

        order_record = {
            "Invoice": invoice_id,
            "Name": name,
            "Phone": phone,
            "Subtotal": subtotal,
            "Tax": tax,
            "Discount": discount,
            "GrandTotal": grand_total,
            "Paid": payment,
            "Due": grand_total - payment,
            "Date": date
        }

        df_order = pd.DataFrame([order_record])

        if os.path.exists("orders.csv"):
            df_order.to_csv("orders.csv", mode='a', header=False, index=False)
        else:
            df_order.to_csv("orders.csv", index=False)

        st.success("Invoice Generated Successfully ☕")
        st.balloons()

        st.json(order_record)
        st.session_state.cart = []
