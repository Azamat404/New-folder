from random import *
comp_number=randint(1,10)
attempts=0
while True:
    number=int(input("Guess the number\t:"))
    attempts+=1
    if number>comp_number:
        print("Press number that will be lower")
    elif number<comp_number:
        print("Press number that will be bigger")
    else: 
        print("You are right") 
        print(F"{attempts} you have got")
        break


