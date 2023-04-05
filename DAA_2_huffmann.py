class node:
	def __init__(self, freq, symbol, left=None, right=None):
		self.freq = freq

		self.symbol = symbol

		self.left = left

		self.right = right

		self.huff = ''


def printNodes(node, val=''):
	newVal = val + str(node.huff)

	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")


chars = list(input("Enter characters : ").split())
# 'a', 'b', 'c', 'd', 'e'

freq = list(map(int,input("Enter the count : ").split()))
# 3 5 6 4 2

nodes = []

for x in range(len(chars)):
	nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
	nodes = sorted(nodes, key=lambda x: x.freq)

	left = nodes[0]
	right = nodes[1]

	left.huff = 0
	right.huff = 1

	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

	nodes.remove(left)
	nodes.remove(right)
	nodes.append(newNode)

print("HUFFMANN CODE")
printNodes(nodes[0])
