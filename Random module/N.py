import random as rnd 
 a=int(input("enter the number from which you want to divide")) 
 for i in range(a): 
     j=int(input("enter the first limit:")) 
     k=int(input("enter the second limit:")) 
     b=rnd.randrange(j,k,a) 
     print(b) 
     break
