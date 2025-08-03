class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

        def deposit(amount):
          return f"Current Balance : {BankAccount.account_balance + amount}"
         

        def withdraw(amount):
            if BankAccount.account_balance > amount:
                BankAccount.account_balance - amount
            else:
                return "Insufficient funds."

        def display_balance():
            return f"$[amount]"