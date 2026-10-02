from config import APP_NAME
from storage import load_transactions
from transactions import (
    add_income,
    add_expense,
    view_transactions,
    edit_transaction,
    delete_transaction
)
from analysis import (
    view_balance,
    category_analysis,
    monthly_summary
)
from charts import (
    category_chart,
    monthly_chart,
    income_vs_expense_chart,
    expense_pie_chart
)


def main():

    transactions = load_transactions()

    while True:

        print(f"\n===== {APP_NAME} =====")

        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Edit Transaction")
        print("6. Delete Transaction")
        print("7. Category Analysis")
        print("8. Monthly Summary")
        print("9. Category Chart")
        print("10. Monthly Chart")
        print("11. Income vs Expense Chart")
        print("12. Expense Pie Chart")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income(transactions)

        elif choice == "2":
            add_expense(transactions)

        elif choice == "3":
            view_transactions(transactions)

        elif choice == "4":
            view_balance(transactions)

        elif choice == "5":
            edit_transaction(transactions)

        elif choice == "6":
            delete_transaction(transactions)

        elif choice == "7":
            category_analysis(transactions)

        elif choice == "8":
            monthly_summary(transactions)

        elif choice == "9":
            category_chart(transactions)

        elif choice == "10":
            monthly_chart(transactions)

        elif choice == "11":
            income_vs_expense_chart(transactions)

        elif choice == "12":
            expense_pie_chart(transactions)

        elif choice == "13":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 13.")


if __name__ == "__main__":
    main()

   