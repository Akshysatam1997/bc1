import hashlib
import datetime
import threading
import time  # Import the time module

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + str(self.timestamp) + str(self.data) +
                               str(self.previous_hash) + str(self.nonce)).encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined:", self.hash)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

class Miner:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def mine(self):
        while True:
            new_block = Block(len(self.blockchain.chain), datetime.datetime.now(),
                              {"miner": "Alice", "amount": 1}, "")
            self.blockchain.add_block(new_block)

            # Print the blockchain
            print("\nBlockchain:")
            for block in self.blockchain.chain:
                print(f"Block {block.index}:")
                print(f"Timestamp: {block.timestamp}")
                print(f"Data: {block.data}")
                print(f"Previous Hash: {block.previous_hash}")
                print(f"Hash: {block.hash}")
                print()

            # Sleep for a while before mining the next block
            # Adjust sleep time to control mining speed
            time.sleep(1)

# Test
if __name__ == "__main__":
    blockchain = Blockchain()
    miner = Miner(blockchain)

    # Start mining in a separate thread
    mining_thread = threading.Thread(target=miner.mine)
    mining_thread.start()

    # Wait for the mining thread to finish
    mining_thread.join()
