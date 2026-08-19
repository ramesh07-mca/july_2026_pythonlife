#TASK-Implement an ATM using OOP

class ATM():

    def __init__(self,bank,location,balance=1000):
        self.bank = bank 
        self.location = location
        self.balance = balance
        self.transactions =[]

    def credit(self):
        amount = float(input("Enter a crediting amount :"))
        if amount <= 0:
            print("Enter a crediting amount")

        else:
            self.balance+= amount
            self.transactions.append(amount)
            print(f"Your credited amount is ${amount}")

    def debit(self):
        amount = float(input("Enter a debiting amount:"))
        if amount > self.balance:
            print("Insufficient balane")    

        else:
            self.balance-= amount
            self.transactions.append(amount) 
            print(f"Your debited amount is ${amount}")

    def check_balance(self):
        print(f"Your current balance is $ {self.balance}")

class atm2(ATM):
    def mini_statement(self):
        if len(self.transactions) == 0:
            print("Your data is not found.")
        else:
            print(self.transactions)

    def exit(self):
        print(f"Thankyou vist again")


object = atm2('SBI','dilsukhnagar',1000)
inp=input("Enter your name:")
while True:

    print("1.credit")
    print("2.debit")
    print("3.check_balance")
    print("4.mini_statement")
    print("5.exit")


    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        object.credit()
    elif choice == "2":
        object.debit()
    elif choice == "3":
        object.check_balance()
    elif choice == "4":
        object.mini_statement()
    elif choice=="5":
        object.exit()
        break
    else:
        print("Please enter valid choice (1-5)")
           
