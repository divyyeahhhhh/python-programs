a=[]
n= int(input("ENTER THE NUMBER OF ELEMENTS:"))
for x in range(0,n):
    element=input("ENTER ELEMENT" + str(x+1) + ":")
    a.append(element)
min1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)<min1):
       min1=len(i)
       temp=i
print("THE WORD WITH SHORTEST LENGTH IS:")
print(temp)
