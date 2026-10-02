import pandas as pd
import matplotlib.pyplot as plt


def create_dataframe(transactions):
    df = pd.DataFrame(transactions)

    if "category" not in df.columns:
        df["category"] = ""

    if "date" not in df.columns:
        df["date"] = ""

    return df


def category_chart(transactions):
    df = create_dataframe(transactions)

    expenses = df[df["type"] == "Expense"]

    if expenses.empty:
        print("No expenses found.")
        return

    result = expenses.groupby("category")["amount"].sum()

    result.plot(kind="bar")

    plt.title("Expense by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def monthly_chart(transactions):
    df = create_dataframe(transactions)

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    expenses = df[df["type"] == "Expense"].copy()

    if expenses.empty:
        print("No expenses found.")
        return

    expenses["month"] = expenses["date"].dt.to_period("M")

    result = expenses.groupby("month")["amount"].sum()

    result.index = result.index.astype(str)

    result.plot(kind="bar")

    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def income_vs_expense_chart(transactions):
    df = create_dataframe(transactions)

    income = df.loc[
        df["type"] == "Income", "amount"
    ].sum()

    expense = df.loc[
        df["type"] == "Expense", "amount"
    ].sum()

    data = pd.Series({
        "Income": income,
        "Expense": expense
    })

    data.plot(kind="bar")

    plt.title("Income vs Expense")
    plt.xlabel("Type")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()


def expense_pie_chart(transactions):
    df = create_dataframe(transactions)

    expenses = df[df["type"] == "Expense"]

    if expenses.empty:
        print("No expenses found.")
        return

    result = expenses.groupby("category")["amount"].sum()

    result.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()