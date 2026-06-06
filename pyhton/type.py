class bankaccount:
    MIN_BALANCE = 100

    def __init__(self,owner,balance=100):
        self.owner=owner
        self._balance=balance
        pass

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"{self.owner}'s balance is: {self._balance}")

        else:
            print("deposit amount should be positive")
            

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <=5
    
account = bankaccount("kyrie",500)
account.deposit(200)

print(bankaccount.is_valid_interest_rate(3))
print(bankaccount.is_valid_interest_rate(10))