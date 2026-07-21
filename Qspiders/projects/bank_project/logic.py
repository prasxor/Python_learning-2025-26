class Bank:
    bank_name = "HDFC"
    manager_name = "rahul"
    no_of_customer = 0
    data_base = []
    
    def __init__(self,c_name,c_age):
        self.c_name = c_name
        self.c_age = c_age
        self.data_base.append(self)
        self.acc_no = "web" + str(self.increment_customer())
        
    @classmethod
    def increment_customer(cls):
        cls.no_of_customer +=1
        return cls.no_of_customer
    
    def all_customers(self):
        for customer in self.data_base:
            print("---------------------------------------------------")
            print(f"customer id : {customer.acc_no}\ncustomer name : {customer.c_name}\ncustomer age : {customer.c_age}\ncustomer bank : {self.bank_name}\nbank manager : {customer.manager_name}")
            print("---------------------------------------------------")
            
    