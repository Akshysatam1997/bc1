class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into {self.name}'s account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.name}'s account. New balance: {self.balance}")
            return True
        else:
            print(f"Insufficient balance in {self.name}'s account.")
            return False

class Transaction:
    @staticmethod
    def transfer(sender, receiver, amount):
        if sender.withdraw(amount):
            receiver.deposit(amount)
            print(f"Transferred {amount} from {sender.name} to {receiver.name}.")
            return True
        else:
            print("Transaction failed.")
            return False

# Test
if __name__ == "__main__":
    alice = Account("Alice", 1000)
    bob = Account("Bob", 500)
    Transaction.transfer(alice, bob, 300)
    print(f"Alice's balance: {alice.balance}")
    print(f"Bob's balance: {bob.balance}")
