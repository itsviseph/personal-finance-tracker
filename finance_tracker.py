# Personal Finance Tracker CLI
# Track income, expenses, balance, and spending by category


# -----------------------------
# Transaction class
# -----------------------------
class Transaction:
    def __init__(self, amount, transaction_type, category, description):
        self.amount = amount
        self.transaction_type = transaction_type  # "income" or "expense"
        self.category = category
        self.description = description


# -----------------------------
# Account class
# -----------------------------
class Account:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

    def get_total_income(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "income":
                total += transaction.amount
        return total

    def get_total_expenses(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                total += transaction.amount
        return total

    def get_expenses_by_category(self):
        category_totals = {}

        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                category = transaction.category
                category_totals[category] = (
                    category_totals.get(category, 0) + transaction.amount
                )

        return category_totals


# -----------------------------
# CLI Application
# -----------------------------
account = Account()

while True:
    print("\n=== Personal Finance Tracker ===")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. View expenses by category")
    print("5. Exit")

    user_action = input("Enter your choice: ").strip()

    if user_action == "1":
        amount = float(input("Enter income amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        transaction = Transaction(
            amount=amount,
            transaction_type="income",
            category=category,
            description=description,
        )

        account.add_transaction(transaction)
        print("Income added successfully.")

    elif user_action == "2":
        amount = float(input("Enter expense amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        transaction = Transaction(
            amount=amount,
            transaction_type="expense",
            category=category,
            description=description,
        )

        account.add_transaction(transaction)
        print("Expense added successfully.")

    elif user_action == "3":
        print(f"Current balance: {account.get_balance()}")

    elif user_action == "4":
        print("\nExpenses by category:")
        expenses = account.get_expenses_by_category()

        if not expenses:
            print("No expenses recorded.")
        else:
            for category, amount in expenses.items():
                print(f"{category}: {amount}")

    elif user_action == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice. Please try again.")
