#Python program to check STRING is pangram using Pythonic Naive Method

#importing string library
import string

#Taking input from user
inputString = input("Enter the string : ")
#declaring varibale and initilize with the all alphabets
allAlphabets = 'abcdefghijklmnopqrstuvwxyz'
#flag value 0
flag = 0
#iteration for all the characters in the allAlphabets variable
for char in allAlphabets:
    #chaking, Is iterated character is in the string{ In Lowercase }
    if char not in inputString.lower():
        #if yes, Flag value updated
        flag = 1
#chacking flag value and pring the result
if flag == 1:
    print("This is not a pangram string");
else:
    print("It is a pangram string")
