t=int(input())
a=list(map(int, input().split()))
a.sort()
day=1
for i in a:
    if i >= day:
        day+=1

print(day-1)
