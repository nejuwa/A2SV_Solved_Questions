t=int(input())
a=list(map(int,input().split()))
a.sort()
    
print(a[(t - 1) // 2])
