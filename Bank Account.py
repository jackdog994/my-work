# Object Oriented Programming Challenge

#For this challenge, create a bank account class that has two attributes:

#* owner
#* balance

#and two methods:

#* deposit
#* withdraw

#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():

    def __init__ (self,owner,balance):

        self.owner = str(owner)
        self.balance = balance

    def more(self):
        more = str(input("Would you like to deposit, withdraw, or are you finished?")).lower()
        if more == "deposit":
            self.deposit()
        elif more == "withdraw":
            self.withdraw()
        elif more == "finished":
            return "OK. Thanks for banking with us today!"
        else:
            print("That's not a valid input! Please try again")
            self.more()
            
    def deposit(self):

        deposit_amount = int(input(f"Hello {self.owner}, your balance is {self.balance} - how much would you like to deposit?"))
        self.balance += deposit_amount
        print(f"Thanks! Your account balance is now {self.balance}")
        self.more()

    def withdraw(self):
        cached_balance = 0
        withdraw_amount = int(input(f"Hello {self.owner}, your balance is {self.balance} - how much would you like to withdraw?"))
        while self.balance >= 0:
            cached_balance = self.balance
            cached_balance -= withdraw_amount
            if  cached_balance < 0:
                withdraw_amount = int(input(f"Oops! Withdrawing that much would mean you're overdrawn. Your balance is {self.balance} - how much would you like to withdraw?"))
                continue
            else:
                    self.balance = cached_balance
                    print(f"Thanks! Your account balance is now {self.balance}")
                    break
        self.more()
