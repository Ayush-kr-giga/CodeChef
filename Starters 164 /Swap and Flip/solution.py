t=int(input())

for cases in range(t):
    n=int(input())
    s=input()
    t=input()
    
    sum_s=0
    sum_t=0
    
    for i in s:
        sum_s+=int(i)
    for j in t:
        sum_s+=int(j)
        
    el=sum_s - sum_t
    
    if sum_s==sum_t:
        print("YES")
    elif el%2==0:
        print("YES")
    else:
        print("NO")
        