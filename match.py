'''
day=int(input("Press day of the Weekend"))
match day: 
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Suturday")
    case 7:
        print("Sunday")
    case _:
        print("this day doesnt exist")
'''
number=int(input("Press number "))
numb2r=int(input("Press number "))
action=input("Press math operation ")
match action:
    case "+":
        print(number+numb2r)
    case "-":
        print(number-numb2r)
    case "*":
        print(number*numb2r)
    case "/":
        print(number//numb2r)
    case _:
        print("wrong action")
        
    
    
    








