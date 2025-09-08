a=int(input("ENTER THE 1ST NUMBER "))
b=int(input("ENTER THE 2ND NUMBER"))
print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION")
d=int(input("ENTER YOU CHOICE "))
if d==1:
      c=a+b
      print("ADDITION OF TWO NUMBER IS ",c)
elif d==2:
     w=a-b
     print("SUBTRACTION OF TWO NUMBER IS ",w)
    
elif d==3:
    s=a*b
    print("MULTIPLICATION OF TWO NUMBER IS ",s)
elif d==4:
    i=a//b
    print("DIVISION OF TWO NUMBER IS ",i)
else:
    
    print("INVALID ")
