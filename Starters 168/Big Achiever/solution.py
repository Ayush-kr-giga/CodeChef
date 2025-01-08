t=int(input())
for cases in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    mood=[0]*n
    m=-1
    for i in range(n):
        if ls[i]>m:
            mood[i]=1 
        m=max(m,ls[i])
        
    for j in mood:
        print(j,end=" ")
    print()
    
        
        