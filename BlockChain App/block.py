class Block():
    
    def __init__(self, data):
        self.hash = None
        self.nonce = 0
        self.data = data
        
    def __str__(self):
        return f"{self.data}{self.nonce}"