sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if avg>=91:
    print("Grade A1")
elif(avg>=81 and avg<90):
    print("Grade: A2")
elif(avg>=71 and avg<80):
    print("Grade: B1")
elif(avg>=61 and avg<70):
    print("Grade: B2")
elif(avg>=51 and avg<60):
    print("Grade: C1")
elif(avg>=41 and avg<50):
   print("Grade: C2")
else:
    print("Grade: D")
