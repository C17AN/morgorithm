
class Trie():
  def __init__(self):
    self.root = {}

  def insert(self, string):
    currentNode = self.root

    for char in string:
      if char not in currentNode:
        currentNode[char] = {}
      currentNode = currentNode[char]

  def search(self, string):
    currentNode = self.root
    index = 0

    for char in string:
      index += 1
      # print(string, char, end = " ")
      if char in currentNode:
        if index == len(string) and len(currentNode[char]):
          return True
        currentNode = currentNode[char]
    return False


T = int(input())
for _ in range(T):
  N = int(input())
  stringArr = []
  trie = Trie()
  stringArr = []
  for _ in range(N):
    temp = input()
    trie.insert(temp)
    stringArr.append(temp)
  isConsistent = True
  for value in stringArr:
    res = trie.search(value)
    if res:
      print("NO")
      isConsistent = False
      break
  if isConsistent:
    print("YES")
  

