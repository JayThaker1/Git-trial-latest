'''
----------------- Explaination --------------------

IConnectCoins(ICC)

t1: Jay sends Kishore 4 ICC
t1: Jaideep sends Kishore 5.6 ICC
t1: Kishore sends Jay 9.3 ICC

def NeuralHash(t1): (SHA256)

B1 ("AAAA", t1, t2, t3) -> 76fd89
B2 (76fd89, t4, t5, t6) -> 8923ff
B3 (8923ff, t7, t8, t9) -> 77ab00


'''
# Coding starts here.

import hashlib

class IConnectCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = '| ' + ' |  | '.join(transaction_list) + " |  | " + previous_block_hash + ' | '
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
        
# Transactions:
t1 = "Jay sends 4 ICC to Kishore"
t2 = "Jaideep sends 5.6 ICC to Jay"
t3 = "Kishore sends 9.0 ICC to Jaideep"
t4 = "Shweta sends 7.4 ICC to Jay"
t5 = "Prathmesh sends 3.0 ICC to Sharvari"
t6 = "Jay sends 5.7.0 ICC to Adnan"

initial_block = IConnectCoinBlock("First Block Initiated", [t1,t2])
print("\n")
print("Block 1:")
print(initial_block.block_data)
print("Block 1 hashes: "+initial_block.block_hash)

second_block = IConnectCoinBlock(initial_block.block_hash, [t3,t4])
print("\n")
print("Block 2:")
print(second_block.block_data)
print("Block 2 hashes: "+second_block.block_hash)

Third_block = IConnectCoinBlock(second_block.block_hash, [t5,t6])
print("\n")
print("Block 3:")
print(Third_block.block_data)
print("Block 3 hashes: "+Third_block.block_hash)

