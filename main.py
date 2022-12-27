class BankAccount:
    balance = 0
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'This account belongs to {self.name}.'
    
    def showBalance(self):
        print(f'You currently have {self.balance}$ in your bank account.') 
        
    def deposit(self, amount):
        if amount <= 0:
            print('Invalid deposit amount.')
        else:
            print(f'You are depositing {amount}$ to your account.') 
            self.balance += amount
            self.showBalance()
    
    def withdraw(self, amount): 
        if self.balance <= 0:
            print('You currently have nothing to withdraw.')
        elif amount <= 0:
            print('Invalid withdrawal amount.')
        else:
            print(f'You are withdrawing {amount}$ from your account.')    
            self.balance -= amount
            self.showBalance()
    
myAccount = BankAccount('Trez')

myAccount.deposit(2000)
print()
myAccount.withdraw(1000)
print()
myAccount.showBalance()