# cook your dish here
t=int(input())

for cases in range(t):
    n,k,p=map(int,input().split())
    chairs=list(map(int,input().split()))
    
    varun=p 
    ved=k 
    
    ved+=max(chairs)
    
    chairs.remove(max(chairs))
    
    for i in chairs:
        varun+=i 
    
    if varun>ved:
        print("VARUN")
    elif ved>varun:
        print("VED")
    else:
        print("EQUAL")