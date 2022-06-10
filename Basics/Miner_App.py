import hashlib
from tkinter import END
from tracemalloc import stop

print("\n\n")
usr_input = input("Enter Message: ")
print("Your Hash: " + hashlib.sha256(usr_input.encode()).hexdigest())

# Basic Settings
NONCE_LIMIT = 100000000000
Zeros = 8

def mine_hash(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * Zeros):
            print(f"Hash Found with NONCE: {nonce}")
            combined_text = str(block_number) + transactions + previous_hash + str(nonce)
            print(hashlib.sha256(combined_text.encode()).hexdigest())
            return hash_try
        
        
    return -1

block_number = input("\nEnter Block Number: ")
transactions = input("\nEnter Transaction: ")
previous_hash = input("\nEnter Previous Hash: ")

print("\nMining Hashes for Nonce....\n")
mine_hash(block_number, transactions, previous_hash)
