def isHappy(n):    
    r = s = 0;    
    while(n > 0):    
        r = n%10    
        s += r**2  
        n //= 10    
    return s  
        
n = int(input("ENTER THE NUMBER:"))    
res = n;    
     
while(res != 1 and res != 4):    
    res = isHappy(res)    
     
if(res == 1):    
    print("TRUE,SINCE IT IS A HAPPY NUMBER")
elif(res == 4):    
    print("FALSE,SINCE IT IS NOT A HAPPY NUMBER")
