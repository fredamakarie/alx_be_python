class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

        def deposit(amount):
          return f"Current Balance: {account_balance + amount}"
         

        def withdraw(amount):
            if account_balance > amount:
                account_balance - amount
            else:
                return "Insufficient funds."

        def display_balance():
            return f"$[amount]"