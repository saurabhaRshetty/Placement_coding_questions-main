def deposit(Accounts, ch, amount):
    if amount > 0:
        Accounts[ch] += amount
        print("Amount Deposited Successfully. New Balance: ", Accounts[ch])
    else:
        print("Invalid deposit amount. Please enter a positive value.")


def menu(Accounts, ch):
    while True:
        print("\nWelcome to Bank Management System")
        print("Account Number:   {}".format(ch))
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Logout")

        try:
            d = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if d == 1:
            print("Your Account Balance is: ", Accounts[ch])
        elif d == 2:
            try:
                amount = int(input("Enter amount to deposit: "))
                deposit(Accounts, ch, amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif d == 3:
            try:
                amt = int(input("Enter amount to withdraw: "))
                if amt > Accounts[ch]:
                    print("Insufficient Balance.")
                elif amt <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    Accounts[ch] -= amt
                    print("Amount Withdrawn Successfully. New Balance: ", Accounts[ch])
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif d == 4:
            try:
                acc_to = int(input("Enter Account Number to transfer: "))
                if acc_to not in Accounts:
                    print("Invalid Account Number.")
                else:
                    amt1 = int(input("Enter amount to transfer: "))
                    if amt1 > Accounts[ch]:
                        print("Insufficient Balance.")
                    elif amt1 <= 0:
                        print("Invalid amount. Please enter a positive number.")
                    else:
                        Accounts[ch] -= amt1
                        Accounts[acc_to] += amt1
                        print(f"Amount Transferred Successfully to {acc_to}. New Balance: {Accounts[ch]}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif d == 5:
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


Accounts = {100: 1000, 101: 1000201, 102: 204393, 103: 4589982}

while True:
    try:
        ch = int(input("\nEnter Account Number (0 to exit): "))
        if ch == 0:
            print("Exiting...")
            break
        elif ch in Accounts:
            menu(Accounts, ch)
            print("Final Account Balance: ", Accounts[ch])
        else:
            print("Invalid Account Number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid account number.")
