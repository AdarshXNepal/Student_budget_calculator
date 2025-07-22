import streamlit as st
import pandas as pd
from analysis import total_spent, category_spent, avg_daily_spent, survival_days,savings_projection
from visulation import plot_category_spent, month_wise_expense


st.set_page_config(page_title="Student Budget Calculator")
# ✅ Custom CSS
st.markdown("""
    <style>
    .stTextInput label, .stDateInput label, .stNumberInput label {
        font-size: 50px !important;
        font-weight: 600;
        
    }
    
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["Date", "Month", "Category", "Product", "Amount"])

st.markdown("""<h1 style='text-align:center;color:#FF6F00; margin-bottom:30px;'> 💰 Student Expenses Tracker </h1>""",unsafe_allow_html=True)

st.header("Enter Details")
col1, col2 = st.columns(2)
with col1:
    total_money = st.number_input("💰 Total money you brought from home (₹):")
with col2:
    planned_days = st.number_input(f"📅 Days to survive :")

st.header(" ✏️ Enter Your Expenses")
with st.form("expense_form", clear_on_submit=True):  # ✅ Clears after submission
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input("Enter the date of the expense(YYYY-MM-DD):")
        categories = ["Food", "Transport", "Books", "Random", "Other"]
        selected = st.selectbox("Select category", categories)
        custom = st.text_input("Or enter a new category")

        category = custom if custom else selected

    with col2:
        month = st.text_input("Month (e.g., July)")
        product = st.text_input("Enter the product name (roll/burger/auto..):")

    amount = st.number_input("Amount", step=10.0)

    submitted = st.form_submit_button("Add Data")
    if submitted:
        new_row = pd.DataFrame(
            [[date, month, category, product, float(amount)]],
            columns=["Date", "Month", "Category", "Product", "Amount"]
        )
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
        st.toast("✅ New Expense Added!")

df = st.session_state.df

st.write("### 📜 All Your Expenses")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  # Always keep datetime64[ns]
st.dataframe(df)

if not df.empty:
    st.markdown("---")
    st.markdown("## 📈 Analysis & Insights")

    # Metrics (Quick Highlights)
    c1, c2, c3,c4 = st.columns(4)
    c1.metric("Total Spent", f"₹{total_spent(df)}")
    c2.metric("Avg Daily Spend", f"₹{round(avg_daily_spent(df).mean(),2)}")
    c3.metric("Survival Days Left", f"{survival_days(df, total_money)} days")
    c4.metric(f"Money left with same Expense after {planned_days} ", f"{savings_projection(df, total_money,planned_days)}")

    # Category Wise Table
    st.markdown("### 🔹 Category-wise Spending")
    st.dataframe(category_spent(df).reset_index(), use_container_width=True)

    # ---------- VISUALIZATIONS ----------
    col1, col2 = st.columns([7,9])
    with col1:
        st.markdown("#### 📊 Spending by Category")
        st.pyplot(plot_category_spent(category_spent(df)))
    with col2:
        st.markdown("#### 📊 Month-wise Spending")
        st.pyplot(month_wise_expense(df))