t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    maxi = 0
    for i in range(0, n, 2):
        maxi = max(maxi, arr[i+1] - arr[i])
    
    print(maxi)
