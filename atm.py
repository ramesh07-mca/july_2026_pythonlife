balance = 0
statement=[]

def credit(amount):
    global balance
    global statement
    balance+=amount
    print(f"${amount} credited to your account.")
    statement.append("+ "+str(amount))
def debit():
    global balance
    global statement
    balance -= amount
    print(f"${amount} debited from your account.")
    statement.append("- "+str(amount))
def balanc(amount):
    global balance
    print(f"Your current balance is: ${balance}")
def ministatement():
    global statement
    print(statement)


while True:
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")
    print("5. Mini_statement")
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        amount = float(input("Enter amount to credit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        else:
            credit(amount)
    

    elif choice == '2':
        amount = float(input("Enter amount to debit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        else:
            debit()
    elif choice == '3':
        print("balance")
        balanc(amount)
       
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    elif choice=='5':
        ministatement()
    else:
        print("Invalid choice. Please try again.")
    