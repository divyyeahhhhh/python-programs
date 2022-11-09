a=int(input("number of items in order:"))
def cost(x):
    if x==1:
        print(750)
    else:
        print(750+(x-1)*200)
cost(a)
