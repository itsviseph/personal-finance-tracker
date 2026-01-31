# -----------------------------
# Account class
# -----------------------------
class Account:
    def __init__(self):
        self.transactions = []
        self.subscriptions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def add_subscription(self, subscription):
        self.subscriptions.append(subscription)

    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

    def get_adjusted_balance(self):
        return self.get_balance() - self.get_monthly_subscription_cost()

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

    def get_monthly_subscription_cost(self):
        total = 0
        for subscription in self.subscriptions:
            if subscription.active:
                total += subscription.amount
        return total

    def get_active_subscriptions_sorted(self):
        active_subscriptions = []

        for subscription in self.subscriptions:
            if subscription.active:
                active_subscriptions.append(subscription)

        active_subscriptions.sort(key=lambda sub: sub.amount, reverse=True)
        return active_subscriptions

    def get_top_subscriptions(self, limit=3):
        return self.get_active_subscriptions_sorted()[:limit]
