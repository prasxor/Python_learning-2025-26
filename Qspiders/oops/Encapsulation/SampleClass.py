class Sample:
    __manager = "ravi sir"

    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    
    def get_salary(self):
        print(f"salary: {self.__salary}")
        
    def set_salary(self, amt):
        self.__salary = amt
        

s1 = Sample("hello", "1.5L")
s1.__salary = "2L"
print(s1.__salary)
s1.get_salary()
