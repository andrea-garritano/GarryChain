import time
import hashlib

class Block:
  def __init__(self, index, previousHash, data, timestamp=None, hash=None): 
    self.index = index
    self.previousHash = previousHash
    self.data = data
    if timestamp == None:
      self.timestamp = int(time.time())
    else:
      self.timestamp = timestamp
    if hash == None:
      self.hash = self.calculateHash()
    else:
      self.hash = hash
    
  def getIndex(self):
    return self.index
  def getPreviousHash(self):
    return self.previousHash
  def getData(self):
    return self.data
  def getTimestamp(self):
    return self.timestamp
  def getHash(self):
    return self.hash
    
  def calculateHash(self):
    hash_obj = hashlib.sha256(str(self.index) + self.previousHash + str(self.timestamp) + self.data)
    hex_dig = hash_obj.hexdigest()
    return hex_dig

class Blockchain:
  chain = []
  def __init__(self):
    self.addGenesisBlock()
    
  def getLastBlock(self):
    return self.chain[-1]

  def addGenesisBlock(self):
    self.chain = [Block(0, "0", "Genesis Block - Hello World", 1494280892, "babf3ad962bb42a46f8324e9a68760cd0cd2e0117ce0394473b15324e2bab82a")]
    
  def addBlock(self, newBlock):
    if (self.isValidChain(newBlock)):
      self.chain.append(newBlock)
      print("! Added a new Block")

  def isValidChain(self, newBlock):
    if (self.getLastBlock().getIndex() + 1 !=newBlock.getIndex()):
      print("! Failed to add Block: invalid index")
      return False
    elif (self.getLastBlock().getHash() != newBlock.getPreviousHash()):
      print("! Failed to add Block: invalid previousHash")
      return False
    elif (newBlock.getHash() != newBlock.calculateHash()):
      print("! Failed to add Block: invalid hash")
      return False
    return True
      
def printLastBlock(): 
  print "Block id: "+str(bc.getLastBlock().getIndex())
  print "Block previousHash: "+str(bc.getLastBlock().getPreviousHash())
  print "Block data: "+bc.getLastBlock().getData()
  print "Block timestamp: "+str(bc.getLastBlock().getTimestamp())
  print "Block hash: "+bc.getLastBlock().getHash()+"\n"

bc = Blockchain()
printLastBlock()
bc.addBlock(Block(1, bc.getLastBlock().getHash(), "My name is Chain, GarryChain"))
printLastBlock()
bc.addBlock(Block(2, bc.getLastBlock().getHash(), "bla bla bla..."))
printLastBlock()
