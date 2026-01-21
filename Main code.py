# assignmentq5(1).py
# Basic Banking System (Main Program)

import project
import random

# Load database at program start
project.load_db()


def create_acc():
    print("----- NEW ACCOUNT -----")

    name = input("Enter your full name: ")
    address = input("Enter your permanent address: ")

    # ID proof (mandatory)
    ID_type = input("Choose your ID proof (ADHAAR / PAN): ").lower()
    if ID_type == "adhaar":
        ID_number = input("Enter your ADHAAR number: ")
    elif ID_type == "pan":
        ID_number = input("Enter your PAN card number: ")
    else:
        print("Invalid ID proof! Account creation failed.")
        return

    # Password (retry until valid)
    while True:
        password = input("Create a 4-digit numeric password: ")
        if password.isdigit() and len(password) == 4:
            break
        else:
            print("Invalid password! Please try again.")

    # Generate unique account number
    while True:
        acc_id = random.randint(10000, 50000)
        if acc_id not in project.accs:
            break

    deposit = int(input("Enter initial deposit amount: "))

    # Store data in database
    project.accs.append(acc_id)
    project.accdetail[acc_id] = deposit
    project.acc_name[acc_id] = name
    project.acc_address[acc_id] = address
    project.acc_idproof[acc_id] = (ID_type, ID_number)
    project.acc_passwords[acc_id] = password

    project.save_db()

    print("\nAccount created successfully!")
    print("Account Number:", acc_id)
    print("Current Balance:", deposit)


def verify_account():
    # Verify account number
    while True:
        accno = input("Enter account number: ")
        if accno.isdigit() and int(accno) in project.accs:
            accno = int(accno)
            break
        else:
            print("Invalid account number! Please try again.")

    # Verify password
    while True:
        password = input("Enter your 4-digit password: ")
        if project.acc_passwords[accno] == password:
            print("Verification successful!")
            return accno
        else:
            print("Incorrect password! Please try again.")


def deposit():
    accno = verify_account()
    amt = int(input("Enter amount to deposit: "))
    project.accdetail[accno] += amt
    project.save_db()
    print("Deposit successful!")
    print("Current balance:", project.accdetail[accno])


def withdraw():
    accno = verify_account()

    balance = project.accdetail[accno]
    amt = int(input("Enter amount to withdraw: "))

    if amt <= 0:
        print("Invalid amount!")
        return

    if amt <= balance:
        project.accdetail[accno] -= amt
        project.save_db()
        print("Withdrawal successful!")
        print("Amount withdrawn:", amt)
        print("Current balance:", project.accdetail[accno])
    else:
        print("Insufficient balance!")


def check_balance():
    accno = verify_account()
    print("Current balance:", project.accdetail[accno])


# ---------------- MENU ----------------
while True:
    print("\n------ OPTIONS ------")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw (Full Balance)")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Please enter a valid number!")
        continue

    op = int(choice)

    if op == 1:
        create_acc()
    elif op == 2:
        deposit()
    elif op == 3:
        withdraw()
    elif op == 4:
        check_balance()
    elif op == 5:
        print("Thank you for using the banking system!")
        project.save_db()
        break
    else:
        print("Invalid choice!")
