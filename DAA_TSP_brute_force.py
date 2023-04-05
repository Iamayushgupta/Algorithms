from sys import maxsize
from itertools import permutations

def travellingSalesmanProblem(n,graph, s):
	vertex = []
	for i in range(n):
		if i != s:
			vertex.append(i)
	min_path = maxsize
	next_path=permutations(vertex)

	for i in next_path:
		curr_weight = 0
		k = s
		for j in i:
			curr_weight += graph[k][j]
			k = j
		curr_weight += graph[k][s]

		min_path = min(min_path, curr_weight)
		
	return min_path

n=int(input("Enter number of cities to be visited : "))
graph1=[]
print("Enter the matrix of the cities :-")
for _ in range(n):
    l=list(map(int,input().split()))
    graph1.append(l)
s=0
print("Minimum cost of it's tour is",travellingSalesmanProblem(n,graph1, s))
