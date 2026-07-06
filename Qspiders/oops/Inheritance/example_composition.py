class Battery:
    
    def charge(self):
        print("battery is charging")
        
class Phone:
    def __init__(self):
        self.batt = Battery()
    
    def plugIn(self):
        print("charger is connected")
        self.batt.charge()
        

p1 = Phone()
p1.plugIn()