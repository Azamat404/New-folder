def parity(number):
    if number%2==0:
        return F"Number {number} is even"
    else: return F"this {number} is odd"
print(parity(int(input("Press your number\t"))))