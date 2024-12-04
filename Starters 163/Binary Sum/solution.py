t=int(input()) 
for i in range(t):
    n,k=map(int,input().split())
    
    if n%2==0:
        possible=n//2
        possible2=n//2
    else:
        possible=(n//2)+1
        possible2=(n//2)
    
    if possible==k or possible2==k:
        print("YES")
    else:
        print("NO")