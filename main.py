from input_module import collect_expenses
from analysis import total_spent,category_spent,avg_daily_spent,survival_days
from visulation import plot_category_spent,month_wise_expense


def main():
    print("Welcome to the Expense Tracker")
    total_money=float(input("Enter the total money you brought from home: "))
    planned_months=int(input("Enter the total number of days you want to survive: "))
    df=collect_expenses()
    print("Expenses Summary")
    print(df)
    print(f"Total Spent -{total_spent(df)}")
    print(f"Categorywise Expense -{category_spent(df)}")

    print(f"Average you spend daily - {avg_daily_spent(df)}")
    print(f"Total Survival Days with your money -{survival_days(df, total_money)}")

    plot_category_spent(category_spent(df))
    month_wise_expense(df)
    
if __name__=='__main__':
    main()

    



    