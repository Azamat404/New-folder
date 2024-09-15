
while True:
    number=int(input("Press your number"))
    if number<0:
            print("Press normal number")
            continue
    for I in range(1,11):
        I*=number
        print(I)
