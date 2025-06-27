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
    charlie = Account("Charlie", 800)

    transactions = [
        {"sender": alice, "receiver": bob, "amount": 300},
        {"sender": bob, "receiver": charlie, "amount": 200},
        {"sender": charlie, "receiver": alice, "amount": 400}
    ]

    for transaction_data in transactions:
        sender = transaction_data["sender"]
        receiver = transaction_data["receiver"]
        amount = transaction_data["amount"]
        Transaction.transfer(sender, receiver, amount)

    print(f"Alice's balance: {alice.balance}")
    print(f"Bob's balance: {bob.balance}")
    print(f"Charlie's balance: {charlie.balance}")
