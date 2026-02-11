# Weather Advice 

temp = int(input("Enter you current temperature: "))

if(temp>30):
    print("Hot")
elif(temp>=20 and temp<=30):
    print("Warm")
elif(temp>=10 and temp<=19):
    print("Cool")
elif(temp<10):
    print("Cold")
else:
    print("Invalid temperature")