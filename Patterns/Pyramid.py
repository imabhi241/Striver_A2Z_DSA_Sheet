l=5
r=5
for i in range(1,6):
    for j in range(1,10):
        if l<=j<=r:
            print("*",end="")
        else:
            print(" ",end="")    
    l-=1
    r+=1
    print()    