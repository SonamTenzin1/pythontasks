score = input("Enter the score: ")

if score.isdigit():
    score = int(score)

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
else:
    print("Invalid score")
