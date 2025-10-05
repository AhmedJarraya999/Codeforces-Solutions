s=input()
l=len(s)
res=""
for i in range(l):
    if s[i].lower() in "aeiou":
        continue
    else:
        res+="."+s[i].lower()
print(res)
    