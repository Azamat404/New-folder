col=0
def number(Chislo):
    I=0
    global col
    while I<len(Chislo):
        if Chislo[I]%2==0:
            col+=1
        I+=1
    print(col)
list1=[1,3,4,6,8,10,20,24]
number(list1)

