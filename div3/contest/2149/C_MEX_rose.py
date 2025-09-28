#TLE FOR COUNTER DICTIONNARY APPROACH


# from collections import Counter

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
    
#     count = Counter(a)
    
#     missing = sum(1 for i in range(k) if count[i] == 0)
    
#     # minimum operations
#     operations = max(missing, count[k])
    
#     print(operations)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    freq = [0] * (n + 2)  # frequency array
    for num in a:
        freq[num] += 1
    
    # Count missing numbers in 0..k-1
    missing = 0
    for i in range(k):
        if freq[i] == 0:
            missing += 1
    
    # Minimum operations
    operations = max(missing, freq[k])
    
    print(operations)

