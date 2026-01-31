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
# Subscription class
# -----------------------------


class Subscription:
    def __init__(self, name, amount, category, billing_cycle_days):
        self.name = name
        self.amount = amount
        self.category = category
        self.billing_cycle_days = billing_cycle_days
        self.active = True
