import pandas as pd


def create_dataframe(transactions):
    df = pd.DataFrame(transactions)

    if "category" not in df.columns:
        df["category"] = ""

    if "date" not in df.columns:
        df["date"] = ""

    return df


def view_balance(transactions):
    df = create_dataframe(transactions)

    total_income = df.loc[
        df["type"] == "Income", "amount"
    ].sum()

    total_expense = df.loc[
        df["type"] == "Expense", "amount"
    ].sum()

    balance = total_income - total_expense

    print("\n===== BALANCE =====")
    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Current Balance:", balance)


def category_analysis(transactions):
    df = create_dataframe(transactions)

    expenses = df[df["type"] == "Expense"]

    if expenses.empty:
        print("No expenses found.")
        return

    result = expenses.groupby("category")["amount"].sum()

    print("\n===== CATEGORY ANALYSIS =====")
    print(result)


def monthly_summary(transactions):
    df = create_dataframe(transactions)

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    month = input("Enter month (YYYY-MM): ")

    expenses = df[
        (df["type"] == "Expense") &
        (df["date"].dt.strftime("%Y-%m") == month)
    ]

    income = df[
        (df["type"] == "Income") &
        (df["date"].dt.strftime("%Y-%m") == month)
    ]

    total_income = income["amount"].sum()
    total_expense = expenses["amount"].sum()
    savings = total_income - total_expense

    print("\n===== MONTHLY SUMMARY =====")
    print("Month:", month)
    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Savings:", savings)