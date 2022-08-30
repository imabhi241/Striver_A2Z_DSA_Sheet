l=5
r=5
l_2=1
r_2=9
for i in range (1,11):
    for j in range(1,10):
        if i<=5:
            if l<=j<=r:
                print("*",end="")
            else:
                print(" ",end="") 
        else:
            if l_2<=j<=r_2:
                print("*",end="")
            else:
                print(" ",end="") 
    if i<=5:
        l-=1
        r+=1
    else:
        l_2+=1
        r_2-=1    
    print()