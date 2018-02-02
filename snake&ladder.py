import random
print(random.randint(1,6))
count=0
while(count<=100):     
    n=input("enter'r' to roll a dice")
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random number is ",r)
        print("your in position",count)
    if count>100:
       count=count-r
       print("your number is greater than 100 roll oce more")
    if count==100:
        print("you have won")
        break
    if count>100:
        print("your number is greater than 100 try again")
           
    elif count==8:
            count=37
            print("your in position",count)
    elif count==11:
            count=2
            print("your in position",count)
    elif count==13:
            count=34
            print("your in position",count)
    elif count==25:
            count=4
            print("your in position",count)
    elif count==38:
            count=9
            print("your in position",count)
    elif count==40:
            count=68
            print("your in position",count)
    elif count==52:
            count=81
            print("your in position",count)
    elif count==65:
            count=46
            print("your in position",count)
    elif count==76:
            count=97
            print("your in position",count)
    elif count==89:
            count=70
            print("your in position",count)
    elif count==93:
            count=64
            print("your in position",count)
    elif count>100:
        
            print ("you have won")
    
       
