def recLS(arr, l, r, x, c):
	if r < l:
		return -1, c
	if arr[l] == x:
		return l, c
	if arr[r] == x:
		return r, c

    c+=1
    
	return recLS(arr, l+1, r-1, x,c)

arr = [12, 34, 54, 2, 3]
n = len(arr)
x = 3
c=0
print(recLS(arr,0,n-1,x,c))



