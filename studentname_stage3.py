def percentage(num1, num2, num3):
    total = num1 + num2 + num3
    return (total / 300) * 100

if __name__ == "__main__":
    student_name = input("Enter the student's name: ")
    first_sub_mark = int(input("Enter the first subject mark(0,100): "))
    second_sub_mark = int(input("Enter the second subject mark(0,100): "))
    third_sub_mark = int(input("Enter the third subject mark(0,100): "))

    result = percentage(first_sub_mark, second_sub_mark, third_sub_mark)

    print("Student Name:", student_name)
    print(f"total marks:{ first_sub_mark + second_sub_mark + third_sub_mark}/300")
    print("Percentage:", result)

    if result >= 75:
        print("Grade: A")
    elif result >= 60:
        print("Grade: B")
    elif result >= 40:
        print("Grade: C")
    else:
        print("Grade: F")