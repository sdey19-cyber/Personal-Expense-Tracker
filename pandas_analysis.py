import json
import pandas as pd

FILE_NAME = "transactions.json"


def load_transactions():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def show_all_transactions(df):
    print("\n===== ALL TRANSACTIONS =====")

    if df.empty:
        print("No transactions found.")
        return

    print(df.to_string(index=False))


def show_expenses(df):
    print("\n===== EXPENSES =====")

    expenses = df[df["type"] == "Expense"]

    if expenses.empty:
        print("No expenses found.")
        return

    print(expenses.to_string(index=False))


def show_income(df):
    print("\n===== INCOME =====")

    income = df[df["type"] == "Income"]

    if income.empty:
        print("No income found.")
        return

    print(income.to_string(index=False))


def category_analysis(df):
    print("\n===== CATEGORY ANALYSIS =====")

    expenses = df[df["type"] == "Expense"]

    if expenses.empty:
        print("No expenses found.")
        return

    result = expenses.groupby("category")["amount"].sum()

    print(result)


def monthly_analysis(df):
    print("\n===== MONTHLY ANALYSIS =====")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    expenses = df[df["type"] == "Expense"].copy()

    if expenses.empty:
        print("No expenses found.")
        return

    expenses["month"] = expenses["date"].dt.to_period("M")

    result = expenses.groupby("month")["amount"].sum()

    print(result)


def total_analysis(df):
    print("\n===== TOTAL ANALYSIS =====")

    total_income = df.loc[
        df["type"] == "Income", "amount"
    ].sum()

    total_expense = df.loc[
        df["type"] == "Expense", "amount"
    ].sum()

    balance = total_income - total_expense

    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Current Balance:", balance)


transactions = load_transactions()


if len(transactions) == 0:
    print("No transaction data found.")

else:
    df = pd.DataFrame(transactions)

    if "category" not in df.columns:
        df["category"] = ""

    if "date" not in df.columns:
        df["date"] = ""

    while True:

        print("\n===== PANDAS EXPENSE ANALYZER =====")
        print("1. View All Transactions")
        print("2. View Expenses")
        print("3. View Income")
        print("4. Category Analysis")
        print("5. Monthly Analysis")
        print("6. Total Analysis")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_transactions(df)

        elif choice == "2":
            show_expenses(df)

        elif choice == "3":
            show_income(df)

        elif choice == "4":
            category_analysis(df)

        elif choice == "5":
            monthly_analysis(df)

        elif choice == "6":
            total_analysis(df)

        elif choice == "7":
            print("Thank you for using Pandas Expense Analyzer!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 7.")