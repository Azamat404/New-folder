class bicycle :
    def __init__(self,wheel,color,motor):
        self.wheel=wheel
        self.color=color
        self.motor=motor
    def stop(self):
        print(F"Bicycle  is stopped")
class Kids(bicycle):
    def __init__(self, wheel,color,motor,horn,prop):
        super().__init__(wheel,color,motor)
        self.horn=horn
        self.prop=prop
    def owner(self):
        print(F"Bicycle owner- {self.prop}")
bicycle1=Kids(4,"green","Yes","Loud","Anton")
print(bicycle1.motor)
print(bicycle1.wheel)
bicycle1.stop()
bicycle1.owner()
