class Bike :
    """
    Документация по созданию мотоцикла:
model — модель,
color — цвет,
top_speed — максимальная скорость
    """
    def __init__(self,model,color,top_speed):
        self.model=model
        self.color=color
        self.top_speed=top_speed
    def beep(self):
        print(F"Sound of model {self.model} -Beep.")
    def __str__(self):
        return F"This object is bike"
bike1=Bike("Yamaha" , "blue" , 300)
bike2= Bike("Ural" , "green" , 120)
print(F"Model {bike1.model} , color {bike1.color} , max speed {bike1.top_speed}cm/h" )
bike1.beep()
print(F"Model {bike2.model} , color {bike2.color} , max speed {bike2.top_speed}cm/h" )
bike2.beep()
print(bike1.__doc__)
print(bike2)