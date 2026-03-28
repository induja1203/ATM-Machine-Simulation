🏧 ATM Machine Simulation (Python + MySQL)

📌 Project Overview

This project is a command-line based ATM simulation system developed using Python and MySQL. It allows users to perform basic banking operations such as account creation, login, balance inquiry, deposit, withdrawal, and viewing transaction history.


 🚀 Features

* 👤 Create Account
* 🔐 Secure Login using Account Number & PIN
* 💰 Check Balance
* ➕ Deposit Money
* ➖ Withdraw Money
* 📜 Transaction History
* 🧭 Menu-driven interface (simulates real ATM behavior)



 🛠️ Technologies Used

* Python
* MySQL
* MySQL Workbench


🗄️ Database Setup

1. Open MySQL Workbench
2. Open the file `atm_db.sql`
3. Execute the script

This will create:

* `users` table
* `transactions` table


 ▶️ How to Run the Project

1. Install required package:

   ```
   pip install mysql-connector-python
   ```

2. Update your MySQL credentials in `atm.py`:

   ```python
   password="YOUR_PASSWORD"
   ```

3. Run the program:

   ```
   python atm.py
   ```

💡 Future Improvements

* Add GUI using Tkinter
* Implement PIN encryption
* Add input validation
* Add OTP verification

🎯 Learning Outcomes

* Database integration with Python
* CRUD operations using MySQL
* Writing modular and structured code
* Building real-world simulation projects


