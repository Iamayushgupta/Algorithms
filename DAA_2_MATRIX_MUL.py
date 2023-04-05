
def matrix_mul(A,B,n,q):
	
    result=[[0]*q]*n

    for i in range(n):
        for j in range(q):
            result[i][j]=0
            for k in range(len(B)):   
                result[i][j] += (A[i][k] * B[k][j])
                print(result)

    return result

A=[]
B=[]
print("Dimensions of First matrix are : ")
n,m=map(int,input().split())
print("Enter element of matrix-1 row by row")
for _ in range(n):
    l=list(map(int,input().split()))
    A.append(l)

print("Dimensions of Second matrix are : ")
p,q=map(int,input().split())
print("Enter element of matrix-2 row by row")
for _ in range(p):
    l=list(map(int,input().split()))
    B.append(l)


if m!=p:
    print("Matrix Multiplication not possible")
else:
    ans=matrix_mul(A,B,n,q)
    print(ans)


