t=int(input())
for _ in range(t):  
    a,b,c,n=map(int,input().split())    
    m = max(a, b, c)
    min_needed = (m - a) + (m - b) + (m - c)
    if n<min_needed:
        print("NO")
    elif (n-min_needed)%3==0:
        print("YES" )
    else:
        print("NO")
    
