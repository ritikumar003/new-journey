
class badbankaccount:
    def __init__(self):
        self.balance=0.0



class bankaccount:
    def __init__(self):
        self._balance=0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self,amount):
        if amount <=0:
            raise ValueError("deposit amount must be positive.")
        self._balance+=amount

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("withdraw amount must be positive.")
        
        if amount>self.balance:
            raise ValueError("withdraw amount must be less.")
        self._balance-=amount

account=bankaccount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)
