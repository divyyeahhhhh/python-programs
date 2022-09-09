n=int(input("ENTER THE NUMBER:"))
while n!=1:
    if n%5==0:
        n=n//5
    elif n%3==0:
        n=n//3
    elif n%2==0:
        n=n//2
    else:
        print('IS NOT A UGLY NUMBER')
        break
else:
    print('IT IS A UGLY NUMBER')
