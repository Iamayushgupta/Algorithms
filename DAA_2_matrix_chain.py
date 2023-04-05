def MatrixChainOrder(p, n):
	m = [[0 for x in range(n)] for x in range(n)]

	for i in range(1, n):
		m[i][i] = 0

	for L in range(2, n):
		for i in range(1, n-L + 1):
			j = i + L-1
			m[i][j] = 1000000
			for k in range(i, j):

				q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
				if q < m[i][j]:
					m[i][j] = q

	return m[1][n-1]


n=int(input("Enter the number of matrices : "))
print("Enter the Dimensions of matrices in order")
arr=[]
for i in range(n):
    n,m=map(int,input().split())
    if i==0:
        arr.append(n)
        arr.append(m)
    else:
        arr.append(m)
        
size = len(arr)

print("Minimum number of multiplications is " +
	str(MatrixChainOrder(arr, size)))
