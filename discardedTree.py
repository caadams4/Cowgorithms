from binarytree import Node

class cowNode:
  def __init__(cowNode, cowID, actionCode, actionInt, timeStamp):
      #Cow node constructor. This is called after reading input to create the new cow node to be inserted. 
    
    cowNode.height = 1
    cowNode.parent = None
    cowNode.left = None
    cowNode.right = None
    cowNode.cowID = cowNode
    cowNode.actionCode = actionCode
    cowNode.actionInt = actionInt
    cowNode.timeStamp = timeStamp

class Cows:
  root = None
  def cowsIncoming(self, cowNode, root):
    if Cows.root == None:
      Cows.root = cowNode
    elif cowNode.cowID < root.cowID:
      # Repeat looking left
      self.cowsIncoming(cowNode, root.left)
    elif cowNode.cowID > root.cowID:
      # Repeat looking right
      self.cowsIncoming(cowNode, root.right)
    # Set root height
    root.height = self.setHeight(self,root)

    # rotation calls 
    #  1
    # -1
    #  1
    # -1
    
    return

  def singleRotRight():
    return

  def singleRotLeft():
    return

  def doubleRotRight():
    return

  def doubleRotLeft():
    return

  def getBalance(self,cowNode):
      
    return

  def setHeight(self,cowNode):
   height = max(self.cowNode.left,self,cowNode.right) + 1
   return height

  def printReport():
    return

with open('cows.txt') as file:
  contents = file.read()
  print(contents)
  cowListRaw = contents.split('\n')
  cowAmount = len(cowListRaw)

  for i in range(cowAmount):
    incomingCow = cowListRaw[i].split(' ')
    cowID = incomingCow[0]
    actionCode = incomingCow[1]
    actionInt = incomingCow[2]
    timeStamp = incomingCow[3]
    print(incomingCow)