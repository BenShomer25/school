while True:
    try:
        students_num = int(input("how many students took the test? "))
    except ValueError:
        print("please input int number")
        continue
    else:
        if students_num >= 1:
            break
        else:
            print("please input int number greater than 0")
            continue

grades = []
for i in range(students_num):
    while True:
        try:
            grade = int(input("grade: "))
            grades.append(grade)
        except ValueError:
            print("please input int number")
            continue
        else:
            if 0 <= grade <= 100:
                break
            else:
                print("please input an int number between 0 and 100")
                continue

average = sum(grades) / students_num

atuda = 0
for g in grades:
    if g > average:
        atuda += 1

if atuda == 0:
    print("no students went to the atuda")
elif atuda == 1:
    print("1 student went to the atuda")
else:
    print(f"{atuda} students went to the atuda")