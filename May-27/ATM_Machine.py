balance = 10000

while True:
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited! New balance: ₹{balance}")
    elif choice == '2':
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"Withdrawn...New balance: ₹{balance}")
    elif choice == '3':
        print(f"Current balance: ₹{balance}")
    elif choice == '4':
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid option")
