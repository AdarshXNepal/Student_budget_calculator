import pandas as pd


def collect_expenses():
    df=pd.DataFrame(columns=["Date","Category","Product","Amount"])

    while True:
        date=input("Enter the date of the expense(YYYY-MM-DD):")
        month=input("Enter the month of the expense (july..)")
        category=input("Enter the category of the expense ( food/travel/stationary ):")
        product=input("enter the product name (roll/burger/auto..):")
        amount=input("enter the amount of the expense:")

        new_row = pd.DataFrame([[date, month, category, product, float(amount)]], columns=["Date", "Month", "Category", "Product", "Amount"])
        df = pd.concat([df, new_row], ignore_index=True)

        more=input("do you want to add more expenses? (y/n):").lower()
        if more!="y":
            break
    
    return df

