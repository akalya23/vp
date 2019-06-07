n=int(input())
a = [int(y) for y in input().split()]
for i in range(0,n):
    if i<n-1:
        b1=' '
    else:
        b1=''
    if i%2==0:
        if a[i]%2!=0:
            print(a[i],end=b1)
    elif i%2!=0:
        if a[i]%2==0:
            print(a[i],end=b1)
