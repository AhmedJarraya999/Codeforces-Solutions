t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    zeros = a.count(0)
    neg = a.count(-1)
    
    ops = zeros  # turn all zeros into 1
    if neg % 2 == 1:
        ops += 2  # turn one -1 → 1 to make product positive
    
    print(ops)
