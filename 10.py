n,m=map(int,input().split())
a1=[int(n) for n in input().split()]
b1=[int(m) for m in input().split()]
cu=0
for i in range(0,len(b1)):
    for j in range(0,len(a1)):
        if b1[i]==a1[j]:
            cu +=1
if cu==len(b1):
    print("YES")
else:
    print("NO")
