import matplotlib.pyplot as plt
from analysis import category_spent


def plot_category_spent(category_spent):
    plt.pie(category_spent,labels=category_spent.index,autopct="%1.1f%%")
    plt.title("Category-wise Expense Distribution")
    plt.show()

def month_wise_expense(df):
    plt.figure(figsize=(10,5))
    df.groupby("Month")["Amount"].sum().plot(kind="bar",color="skyblue")
    plt.title("Month-wise Expense")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

