import threading
import time


class BankAccount:
    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, amount: float):
        with self.lock:
            balance = self.balance
            # Mimic a context switch
            time.sleep(2)
            self.balance = balance + amount

    def withdraw(self, amount: float):
        with self.lock:
            balance = self.balance
            self.balance = balance - amount


account = BankAccount()
print(f"The account balance is: £ {account.balance}")
print("Deposit £ 100.00")
t1 = threading.Thread(target=account.deposit, args=(100.0,))
print("Withdraw £ 50.00")
t2 = threading.Thread(target=account.withdraw, args=(50.0,))
t1.start()
t2.start()
t1.join()
t2.join()

print(f"The account balance is: £ {account.balance}")
