n = int(input())
target = n - 10
res = 0

if 2 <= target <= 9:
    res = 4
elif target == 10:
    res = 15
elif target == 11:
    res = 4
else:
    res = 0

print(res)
