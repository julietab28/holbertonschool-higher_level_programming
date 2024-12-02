#!/usr/bin/python3

class BankAccount():
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = amount + self.__balance
        return self.__balance
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return self.__balance
        return "Error"
    def get_balance(self):
        return self.__balance

account = BankAccount(100)
print(account.deposit(50))
print(account.withdraw(151))
print(account.get_balance())


