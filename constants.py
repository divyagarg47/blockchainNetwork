BLOCK = 1 
BLOCKCHAIN = 2 
TRANSACTION = 3
ACCESS = 4 

class Transaction:
    def __init__(self,index) -> None:
        self.index = index 
    def __str__(self):
        return f"Transaction #{self.index}"
class Message:
    def __init__(self,messagebody,type):
        self.messagebody = messagebody
        self.type = type
    
    def getMessageBody(self):
        return self.messagebody
class Block:
    def __init__(self, index):
        self.index = index

    @staticmethod
    def create_genesis_block():
        # Manually create the first block (genesis block)
        return Block(0)

    def __str__(self):
        return f"Block #{self.index}"