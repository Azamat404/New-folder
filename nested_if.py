'''
x=int(input("Enter your number : "))
y=int(input("Enter your number : "))
if x>0:
    if y>0:
        print("this number is in 1 quarter ")
    else:print("this number is in 4 quarter ")
else:  
    if y<0 :
        print("this number is in 3 quarter ")
    else:print("this number is in 2 quarter ")
'''
year=int(input("Enter year: "))
if year%4==0:
    print("this  is leap year")
else:print("this is not a leap year")
