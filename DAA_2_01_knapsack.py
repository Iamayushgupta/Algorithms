def knapSack(W, wt, val, n):
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]

	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1]
						+ K[i-1][w-wt[i-1]],
							K[i-1][w])
			else:
				K[i][w] = K[i-1][w]

	return K[n][W]


profits = list(map(int,input("profit values : ").split()))
#100 160 50 200
wt = list(map(int,input("weights : ").split()))
#10 20 30 40
max_wt = int(input("Maximum weight : "))
#60
n = len(profits)
print("The total maximum profit with weight",max_wt,"is"
    ,knapSack(max_wt, wt, profits, n))

