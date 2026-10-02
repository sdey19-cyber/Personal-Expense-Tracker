from datetime import datetime


def get_positive_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Invalid amount! Please enter a number.")


def get_required_text(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD format.")