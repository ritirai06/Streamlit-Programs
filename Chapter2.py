import streamlit as st
import pandas as pd
from datetime import datetime

# ===========================
# PAGE CONFIG
# ===========================
st.set_page_config(
    page_title="Chai Maker & Billing App",
    page_icon="🍵",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ===========================
# GLOBAL STYLING
# ===========================
st.markdown("""
<style>
    .main {padding:20px}
    .title {
        text-align:center;
        font-size:40px;
        font-weight:800;
        color:#4b2e2e;
    }
    .price-box {
        background:#fff6e6;
        padding:15px;
        border-radius:15px;
        border:1px solid #ffdd99;
    }
    .footer {
        text-align:center;
        color:gray;
        font-size:13px;
        margin-top:30px;
    }
            
</style>
""", unsafe_allow_html=True)



# ===========================
# HEADER
# ===========================
st.markdown('<div class="title">🍵 Welcome to the Chai Maker App!</div>', unsafe_allow_html=True)

st.markdown("---")

# ===========================
# CHAI ORDER SECTION
# ===========================
st.title("✨ Chai Order Section")

with st.container():
    st.subheader(" Prices per cup")
    st.write("Masala Chai – ₹30")
    st.write("Ginger Chai – ₹15")
    st.write("Cardamom Chai – ₹20")
    st.write("Tulsi Chai – ₹10")
    st.markdown('<div class="price-box">Note: Prices may vary based on customization.</div>', unsafe_allow_html=True)

chai_prices = {
    "Masala Chai": 30,
    "Ginger Chai": 15,
    "Cardamom Chai": 20,
    "Tulsi Chai": 10
}

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛠 Customize Your Chai")
        chai_type = st.radio(
            "Choose Chai Type:",
            ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai"]
        )

        milk_option = st.selectbox(
            "Milk Type:",
            ["Whole Milk", "Skim Milk", "Almond Milk", "Oat Milk"]
        )

        water_level = st.slider(
            "Water Level (cups)",
            0, 5, 3
        )

        sugar_level = st.slider(
            "Sugar Level (tsp)",
            0, 5, 2
        )

    with col2:
        st.subheader("📦 Order Details")
        cups = st.number_input("Number of Cups", 1, 10, 1)
        customer_name = st.text_input("Your Name")

        if st.button("Make My Chai 🍶"):
            if customer_name:
                st.toast(f"Hello {customer_name}! your chai order is being processed. ☕")
                st.success(
                    f"Hello {customer_name}! Your {cups} cup(s) of {chai_type} "
                    f"with {milk_option}, {water_level} cups water and "
                    f"{sugar_level} tsp sugar are being prepared."
                )
                st.balloons()
            else:
                st.warning("Please enter your name to proceed.")

st.info(f"🫶 You selected **{milk_option}**, **{water_level} cups water**, **{sugar_level} tsp sugar**")

chai_total = cups * chai_prices[chai_type]
st.success(f"Total Chai Cost: ₹{chai_total}")

st.markdown("---")

# ===========================
# BILLING SECTION
# ===========================
st.header("🧾 Invoice / Billing Section")

with st.container():
    st.subheader("👤 Customer Details")
    name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    address = st.text_area("Address")
    date = st.date_input("Date", datetime.now())
    time = st.time_input("Time", datetime.now().time())

st.subheader("🛍 Items Purchased")
num_items = st.number_input("Number of Items", 1, 50)

items = []
for i in range(int(num_items)):
    with st.expander(f"Item {i+1}"):
        selected_item = st.selectbox(f"Select Item {i+1}", list(chai_prices.keys()), key=f"select{i}")
        item= selected_item
        qty = st.number_input(f"Quantity {i+1}", 1, 1000, key=f"qty{i}")
        price = st.number_input(f"Unit Price {chai_prices}", 0.0, 10000.0, key=f"price{i}")
        total = qty * price
        st.write(f"Total: ₹{total:.2f}")
        items.append([item, qty, price, total])

df = pd.DataFrame(items, columns=["Item", "Qty", "Unit Price", "Total"])

st.subheader("📊 Bill Summary")
st.table(df)

subtotal = df["Total"].sum()
tax = subtotal * 0.18
grand_total = subtotal + tax

st.success(f"Subtotal: ₹{subtotal:.2f}")
st.warning(f"Tax (18%): ₹{tax:.2f}")
st.error(f"Grand Total: ₹{grand_total:.2f}")

pickup_date = st.date_input("Pickup Date")
pickup_time = st.time_input("Pickup Time")
payment_amount = st.number_input("Payment Received", min_value=0.0, step=10.0)

if st.button("Confirm Order ✅"):
    st.success("Invoice generated successfully!")
    st.snow()
    st.toast("Chai Order & Invoice Recorded Successfully ☕")

st.markdown('<div class="footer">Made with ❤️ in Streamlit</div>', unsafe_allow_html=True)
