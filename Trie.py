class Trie:
  def __init__(self):
    self.root = {}

  def insert(self, string):
    currentNode = self.root

    for char in string:
      if char not in currentNode:
        currentNode[char] = { }
      currentNode = currentNode[char]
  
  def search(self, string):
    currentNode = self.root

    for char in string:
      if char in currentNode:
        currentNode = currentNode[char]
      else:
        return False
    return True


trie = Trie()
print("Input String : ",end="")
string = input()
print("Input Prefix to validate : ", end = "")
toFind = input()
trie.insert(string)
print("Is '{}' is prefix of '{}' : {}".format(toFind, string, trie.search(toFind)))
