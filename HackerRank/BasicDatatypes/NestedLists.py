if __name__ == '__main__':
    students = []
    scoreList = []
    nameList = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    for student in students:
        scoreList.append(student[1])

    scoreList = sorted(set(scoreList))
    secondLowest = scoreList[1]

    for name, score in students:
        if score == secondLowest:
            nameList.append(name)

    nameList = sorted(nameList)

    for name in nameList:
        print(name)