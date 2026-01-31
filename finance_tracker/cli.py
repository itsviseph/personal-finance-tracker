# finance_tracker/cli.py

from finance_tracker.models import Transaction, Subscription
from finance_tracker.account import Account


def run():
    # -----------------------------
    # CLI Application
    # -----------------------------
    account = Account()

    def get_float_input(prompt):
        while True:
            user_input = input(prompt)

            try:
                value = float(user_input)
                return value
            except ValueError:
                print("Invalid input. Please enter a number.")

    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add income")
        print("2. Add expense")
        print("3. View balance")
        print("4. View expenses by category")
        print("5. View all transactions")
        print("6. Search transactions")
        print("7. Add subscription")
        print("8. View subscriptions")
        print("9. View monthly subscription cost")
        print("10. View adjusted balance")
        print("11. View top subscriptions")
        print("12. Exit")

        user_action = input("Enter your choice: ").strip()

        if user_action == "1":
            amount = get_float_input("Enter income amount: ")
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
            amount = get_float_input("Enter expense amount: ")
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
            print("\nTransaction History:")

            if not account.transactions:
                print("No transactions recorded yet.")
            else:
                for transaction in account.transactions:
                    t_type = transaction.transaction_type.upper()
                    amount = transaction.amount
                    category = transaction.category
                    description = transaction.description

                    print(f"[{t_type}] {amount} | {category} | {description}")

        elif user_action == "6":
            if not account.transactions:
                print("No transactions recorded yet.")
            else:
                user_search = input("Search transaction: ").strip().lower()
                found = False

                for transaction in account.transactions:
                    if (
                        user_search in transaction.category.lower()
                        or user_search in transaction.description.lower()
                        or user_search in str(transaction.amount)
                    ):
                        print(
                            f"[{transaction.transaction_type.upper()}] "
                            f"{transaction.amount} | {transaction.category} | {transaction.description}"
                        )
                        found = True

                if not found:
                    print("No transactions found for this search.")

        elif user_action == "7":
            name = input("Enter subscription name: ")
            amount = get_float_input("Enter subscription amount: ")
            category = input("Enter category: ")
            billing_cycle_days = get_float_input("Enter billing cycle days: ")

            subscription = Subscription(
                name=name,
                amount=amount,
                category=category,
                billing_cycle_days=billing_cycle_days,
            )
            account.add_subscription(subscription)
            print("Subscription added successfully.")

        elif user_action == "8":
            print("\nYour current subscriptions:")

            if not account.subscriptions:
                print("No subscriptions recorded yet.")
            else:
                for subscription in account.subscriptions:
                    name = subscription.name.upper()
                    amount = subscription.amount
                    category = subscription.category
                    billing_cycle = subscription.billing_cycle_days

                    print(f"[{name}] {amount} | {category} | {billing_cycle} days")

        elif user_action == "9":
            total = account.get_monthly_subscription_cost()
            print(f"Your monthly subscription cost is: {total}")

        elif user_action == "10":
            balance = account.get_adjusted_balance()
            print(f"Your adjusted balance is: {balance}")

        elif user_action == "11":
            limit_input = input("How many top subscriptions? (default 3): ").strip()

            if limit_input == "":
                limit = 3
            else:
                limit = int(limit_input)

            top_subs = account.get_top_subscriptions(limit)

            if not top_subs:
                print("No active subscriptions.")
            else:
                print("\nTop subscriptions:")
                for sub in top_subs:
                    print(f"{sub.name} | {sub.amount} | {sub.billing_cycle_days} days")

        elif user_action == "12":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Please try again.")
