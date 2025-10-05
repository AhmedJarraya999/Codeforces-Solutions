n = int(input())
t = input()

i = 0
step = 1
res = ""

while i < n:
    res += t[i]
    i += step
    step += 1

print(res)
