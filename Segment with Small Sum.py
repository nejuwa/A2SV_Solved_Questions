n,s = map(int,input().split())
a= list(map(int, input().split()))
tot= 0 
l,r = 0,0
cnt = 0 
while r< n:
    tot += a[r]
    if tot > s:
        tot -= a[l]
        l+=1

    cnt = max(cnt, r-l +1)
    r+=1
print(cnt)
    
    

    
