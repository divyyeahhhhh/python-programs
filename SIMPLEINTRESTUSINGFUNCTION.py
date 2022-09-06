# Python program to calculate simple interest using function

def calculate_simple_interest(P, R, T):
    # calculate simple interest
    SI = (P * R * T) / 100
    return SI;

if __name__ == '__main__':
    # store the inputs
    P = float(input('Enter principal amount: '))
    R = float(input('Enter the interest rate: '))
    T = float(input('Enter time: '))

    # calling function
    simple_interest = calculate_simple_interest(P, R, T)
    # display result
    print('Simple interest = %.2f' %simple_interest)
    print('Total amount = %.2f' %(P + simple_interest))
