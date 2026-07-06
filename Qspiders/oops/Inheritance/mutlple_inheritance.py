class State:
    state_name = 'telnagana'
    

class Hyderabad(State):
    district = 'hyderabad'

    def district_details(self):
        print(f"district name : {self.district} and state name {self.state_name}\n")
        

class Rangareddy(State):
    district = 'rangareddy'
    
    def district_details(self):
        print(f"district name : {self.district} and state name {self.state_name}\n")
        
h1 = Hyderabad()
h1.district_details()

r1 = Rangareddy()
r1.district_details()