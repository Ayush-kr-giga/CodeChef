t=int(input())
for cases in range(t):
    n=int(input())
    A=input()
    B=input()
    
    
    sure=0
    extra=0
    for i in range(len(A)):
        if int(A[i])==1 and int(B[i])==1:
            sure+=1
        elif int(A[i])==1 or int(B[i])==1:
            extra+=1
    
    # print("SURE ",sure)
    # print("EXTRA ",extra)
    
    if sure%2!=0:
        print("YES")
    else:
        if extra!=0:
            print("YES")
        else:
            print("NO")
            
            
            