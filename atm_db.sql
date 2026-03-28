CREATE DATABASE atm_db;
USE atm_db;

CREATE TABLE users (
    account_number INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    pin INT,
    balance FLOAT DEFAULT 0
);

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_number INT,
    type VARCHAR(20),
    amount FLOAT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_number) REFERENCES users(account_number)
);