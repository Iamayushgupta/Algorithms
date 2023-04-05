n=int(input("Number of itmes : "))
# 4

weights = list(map(int,input("weights : ").split()))
# 10 40 20 30

profits=list(map(int,input("profits : ").split()))
# 60 40 100 120

max_wt= int(input("Maximum weight : "))
# 50

ratio = []
for i in range(n):
    temp = profits[i] / weights[i]
    temp = float("{0:.2f}".format(temp))
    ratio.append([temp,i])

ratio.sort(reverse=True)
carry=0
j=0
net_prof=0
while carry<max_wt:
    wt = weights[ratio[j][1]]
    prof = profits[ratio[j][1]]
    if (carry + wt)<=max_wt:
        carry+=wt
        net_prof+=prof
    else:
        wt_left = max_wt - carry

        net_prof += (ratio[j][0]*wt_left)
        break
    j+=1

print("The Maximum profit is",net_prof)



