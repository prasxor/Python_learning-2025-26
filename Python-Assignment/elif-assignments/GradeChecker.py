# Grade Checker

userGrade = int(input("Enter your grade: "))

if(userGrade>=90 and userGrade<=100):
    print("wow! you got 'A' Grade")
elif(userGrade>=80 and userGrade<90):
    print("Amazing, you got 'B' Grade")
elif(userGrade>=70 and userGrade<80):
    print("Focus, you got 'C' Grade")
elif(userGrade>=60 and userGrade<70):
    print("Good, you got 'D' Grade")
else:
    print("Grades doesn't matters, if you have a skills, you're Failed")