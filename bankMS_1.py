class Account:

    def __init__(self, username, password, balance=0):

        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount
            self.transactions.append(f"Deposited: ${amount}")
            print("Amount deposited:", amount)
            print("Current balance:", self.balance)
        else:
            print("Enter a valid amount")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient amount")
        else:
            self.balance-=amount 
            self.transactions.append(f"Withdraw: ${amount}")
            print("Amount debited: ",amount)
            print("Current balnce: $",self.balance)

    def check_balance(self,):
        print(f"Your current balance is $ {self.balance}")

    def mini_statement(self,):
        print(f"Username: {self.username}")
        if len(self.transactions)==0:
            print("No Transactions")
        else:
            print(f"Your transactions: {self.transactions}")


class SavingsAccount(Account):

    def __init__(self, username, password, balance=0):

        super().__init__(username, password, balance)
    def show_account_type(self):
        print("Account Type: Savings Account")

class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, username, password):

        if username in self.accounts:
            print("Username already exists")

        else:
            account = SavingsAccount(username, password)
            self.accounts[username] = account
            print("Account created successfully") 

    def login(self, username, password):

        if username in self.accounts:

            account = self.accounts[username]
            if account.password == password:
                print("Login successful")
                return account

            else:
                print("Invalid password")

        else:
            print("Invalid username")

        return None

bank = Bank()
while True:

    print("\n------ PYTHON BANK ------")

    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice== "1":
        username=input("Enter username: ")
        password=input("Enter New password:")
        bank.create_account(username,password)

    elif choice=="2":
        username=input("Enter Usename:")
        password=input("Enter Password:")
        account= bank.login(username,password)

        if account is not None:
            while True:

                print("\n------ ACCOUNT MENU ------")

                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Mini Statement")
                print("5. Account Type")
                print("6. Logout")

                choice = input("Enter your choice (1-6): ")

                if choice=="1":
                    amount=int(input("Enter amount to deposit: "))
                    account.deposit(amount)
                elif choice=="2":
                    amount=int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                elif choice=="3":
                    account.check_balance()
                elif choice=="4":
                    account.mini_statement()
                elif choice=="5":
                    account.show_account_type()
                elif choice=="6":
                    print("Logout Successfully")
                    break 
                else:
                    print("Please enter valid choice")
    elif choice=="3":
        print("Thankyou for choosing python bank")
        break
    
    