import pandas as pd

def total_spent(df):
    return df["Amount"].sum()

def category_spent(df):
    return df.groupby("Category")["Amount"].sum()

def product_most_expense(df):
    return df.groupby('Product')["Amount"].sum().sort_values(ascending=False)

def avg_daily_spent(df):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    first_date = df["Date"].min()
    last_date = df["Date"].max()
    days_passed = (last_date - first_date).days + 1
    return total_spent(df) / days_passed if days_passed > 0 else 0

def survival_days(df, total_brought):
    total_remaining = total_brought - total_spent(df)
    daily_avg = avg_daily_spent(df)
    if daily_avg <= 0:
        return 0
    return max(0, round(total_remaining / daily_avg))

def savings_projection(df, total_brought, planned_days):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    spent_so_far = total_spent(df)
    daily_avg = avg_daily_spent(df)
    if daily_avg <= 0:
        return total_brought

    first_date = df["Date"].min()
    last_date = df["Date"].max()
    days_passed = (last_date - first_date).days + 1

    remaining_days = max(0, planned_days - days_passed)
    future_spending = daily_avg * remaining_days
    remaining = total_brought - spent_so_far - future_spending
    return round(remaining, 2)