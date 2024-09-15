
def calculate__average(grades):
    return sum(grades)/len(grades)
def find__highest__grade(grades):
    return max(grades)
def find__lowest__grade(grades):
    return min(grades)
def above__average__students(grades):
    print(grades)
    agrade=sum(grades)/len(grades)
    col=0
    for I in grades: 
        if I>agrade:
            col+=1
    return col
students=int(input( "Как много учащихся?  "))
grades=[]
if students<2:
    print("Слишком мало студентов")
    raise breakpoint
for I in range(students):
    grade=float(input("Какие у них отценки?  "))
    grades.append(grade)
a=calculate__average(grades)
b=find__highest__grade(grades)
c=find__lowest__grade(grades)
d=above__average__students(grades)
print(F"average grade is {a}, the highest grades is {b} , and the lowest grades is {c} ,{d}")
