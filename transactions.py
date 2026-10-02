from storage import save_transactions
from validators import get_positive_amount, get_required_text, get_date


def add_income(transactions):
    amount = get_positive_amount("Enter your income amount: ")
    description = get_required_text("Enter income description: ")
    date = get_date()

    transaction = {
        "type": "Income",
        "amount": amount,
        "description": description,
        "date": date
    }

    transactions.append(transaction)
    save_transactions(transactions)

    print("Income added successfully!")


def add_expense(transactions):
    amount = get_positive_amount("Enter your expense amount: ")
    category = get_required_text("Enter expense category: ")
    description = get_required_text("Enter expense description: ")
    date = get_date()

    transaction = {
        "type": "Expense",
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    transactions.append(transaction)
    save_transactions(transactions)

    print("Expense added successfully!")


def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return

    print("\n===== TRANSACTIONS =====")

    for index, transaction in enumerate(transactions, start=1):
        print(f"Transaction No: {index}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: {transaction['amount']}")

        if transaction["type"] == "Expense":
            print(f"Category: {transaction.get('category', '')}")

        print(f"Description: {transaction['description']}")
        print(f"Date: {transaction.get('date', 'Not available')}")
        print("-------------------------")


def edit_transaction(transactions):
    if not transactions:
        print("No transactions available to edit.")
        return

    view_transactions(transactions)

    try:
        number = int(input("Enter transaction number to edit: "))

        if number < 1 or number > len(transactions):
            print("Invalid transaction number.")
            return

        transaction = transactions[number - 1]

        print("\n===== EDIT TRANSACTION =====")

        amount = get_positive_amount("Enter new amount: ")

        if transaction["type"] == "Expense":
            category = get_required_text("Enter new category: ")
            transaction["category"] = category

        description = get_required_text("Enter new description: ")
        date = get_date()

        transaction["amount"] = amount
        transaction["description"] = description
        transaction["date"] = date

        save_transactions(transactions)

        print("Transaction updated successfully!")

    except ValueError:
        print("Invalid input!")


def delete_transaction(transactions):
    if not transactions:
        print("No transactions available to delete.")
        return

    view_transactions(transactions)

    try:
        number = int(input("Enter transaction number to delete: "))

        if number < 1 or number > len(transactions):
            print("Invalid transaction number.")
            return

        transaction = transactions[number - 1]

        print("\nYou selected:")
        print("Type:", transaction["type"])
        print("Amount:", transaction["amount"])

        confirm = input(
            "Are you sure you want to delete this transaction? (yes/no): "
        )

        if confirm.lower() == "yes":
            del transactions[number - 1]

            save_transactions(transactions)

            print("Transaction deleted successfully!")

        else:
            print("Transaction deletion cancelled.")

    except ValueError:
        print("Invalid input!")