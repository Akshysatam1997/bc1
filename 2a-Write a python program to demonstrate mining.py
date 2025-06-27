import hashlib 
import random 
 
def mine_block(previous_hash, transactions, difficulty):  
    prefix = '0' * difficulty 
    nonce = 0 
    while True: 
        nonce_str = str(nonce)  
        block_content = previous_hash + transactions + nonce_str 
        hash_value = hashlib.sha256(block_content.encode()).hexdigest()  
        if hash_value.startswith(prefix):  
            print(f"Block mined: Nonce = {nonce}, Hash = {hash_value}") 
            return hash_value, nonce 
         
        nonce += 1 
 
if __name__ == "__main__":  
    previous_hash = "0000000000000000000000000000000000000000000000000000000000000000" 
    transactions = "Transaction data goes here" 
    difficulty = 4  
    mined_hash, nonce_used = mine_block(previous_hash, transactions, difficulty)  
    print(f"Mining successful! Mined Hash: {mined_hash}, Nonce used: {nonce_used}") 
