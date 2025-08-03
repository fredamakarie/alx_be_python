class BankAccount:
    def __init__(self, account_balance):
        self.account_balance= account_balance

        def deposit(amount):
            amount + BankAccount.account_balance

        def withdraw(amount):
            if BankAccount.account_balance > amount:
                BankAccount.account_balance - amount
            else:
                return "Insufficient funds."

        def display_balance():
            return f"$[amount]"