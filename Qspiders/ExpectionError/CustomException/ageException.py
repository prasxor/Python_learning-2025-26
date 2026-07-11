
def sample():
    class AgeException(Exception):
        pass
    userAge = int(input("Enter your age: "))
    try:
        if userAge>=18:
            print("You're eligible for voting")
        else:
            raise AgeException("You're not eligible for voting")
    except:
        print(f"Please come after {18-userAge} years later.")
        sample()
sample()