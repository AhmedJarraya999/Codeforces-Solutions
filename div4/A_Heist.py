n=int(input())
arr = list(map(int, input().split()))  # read all numbers on one line
mini=float('inf')
maxi=float('-inf')

for x in arr:  
    mini = min(mini, x)
    maxi = max(maxi, x)

print((maxi - mini + 1) - n)


