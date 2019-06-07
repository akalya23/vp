ni=input()
c1=1
for i in range(len(ni)-1):
    a=ni[i]+ni[i+1]
    b=int(a)
    if b<=26 and ni[i]!="0":
        c1+=1
if c1==3:
    print(c1)
else:
    print(c1+(c1-1)//2)
