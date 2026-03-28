import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your password",
        database="atm_db"
    )
    cursor = conn.cursor()
    print("Connected successfully!")

except Exception as e:
    print("Error:", e)
#Account Creation
def create_account():
    name = input("Enter your name: ")
    pin = int(input("Set your PIN: "))
    balance = float(input("Enter initial deposit: "))

    query = "INSERT INTO users (name, pin, balance) VALUES (%s, %s, %s)"
    values = (name, pin, balance)

    cursor.execute(query, values)
    conn.commit()

    print("Account created successfully!")
    print("Your Account Number is:", cursor.lastrowid)


#Login System
def login():
    acc_no = int(input("Enter account number: "))
    pin = int(input("Enter PIN: "))

    query = "SELECT * FROM users WHERE account_number=%s AND pin=%s"
    cursor.execute(query, (acc_no, pin))

    user = cursor.fetchone()

    if user:
        print("Login successful!")
        return acc_no
    else:
        print("Invalid account number or PIN")
        return None
#Balance check
def check_balance(acc_no):
    cursor.execute("SELECT balance FROM users WHERE account_number=%s", (acc_no,))
    balance = cursor.fetchone()[0]
    print("Your balance is:", balance)
#Money Deposit
def deposit(acc_no):
    amount = float(input("Enter amount to deposit: "))

    cursor.execute("UPDATE users SET balance = balance + %s WHERE account_number=%s", (amount, acc_no))
    
    cursor.execute("INSERT INTO transactions (account_number, type, amount) VALUES (%s, %s, %s)",
                   (acc_no, "Deposit", amount))

    conn.commit()
    print("Deposit successful!")
#Money Withdrawl
def withdraw(acc_no):
    amount = float(input("Enter amount to withdraw: "))

    cursor.execute("SELECT balance FROM users WHERE account_number=%s", (acc_no,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE account_number=%s", (amount, acc_no))

        cursor.execute("INSERT INTO transactions (account_number, type, amount) VALUES (%s, %s, %s)",
                       (acc_no, "Withdraw", amount))

        conn.commit()
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")
#Transaction history
def transaction_history(acc_no):
    cursor.execute(
        "SELECT type, amount, date FROM transactions WHERE account_number=%s",
        (acc_no,)
    )

    records = cursor.fetchall()

    print("\nTransaction History:")
    for row in records:
        print(row)
while True:
    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        create_account()

    elif choice == '2':
        user = login()
        if user:
            while True:
                print("\n1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transactions")
                print("5. Logout")

                option = input("Choose: ")

                if option == '1':
                    check_balance(user)
                elif option == '2':
                    deposit(user)
                elif option == '3':
                    withdraw(user)
                elif option == '4':
                    transaction_history(user)
                elif option == '5':
                    break

    elif choice == '3':
        break
