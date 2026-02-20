def process_scores(students_dict):
    result = {}
    for student, scores in students_dict.items():
        average = sum(scores) / len(scores)  # with 2 decimal places
        result[student] = f"{average:.2f}"

    return result  

def classify_grades(students_dict):
    result = {}
    for student, avg in students_dict.items():
        avg = float(avg)  # Convert string to float
        if avg >= 90:
            result[student] = ("A", avg)
        elif avg >= 75 and avg < 90:
            result[student] = ("B", avg)
        elif avg >= 60 and avg < 75:
            result[student] = ("C", avg)
        else:
            result[student] = ("F", avg)

    return result

def generate_report(classified, passing_avg=70):
#     ===== Student Grade Report =====
# Alice     | Avg: 86.25 | Grade: B | Status: PASS
# Bob       | Avg: 62.50 | Grade: C | Status: PASS
# Clara     | Avg: 96.25 | Grade: A | Status: PASS
# ================================
# Total Students : 3
# Passed         : 3
# Failed         : 0

    report = "===== Student Grade Report =====\n"
    total_students = len(classified)
    passed_students = 0
    failed_students = 0

    for student, (grade, avg) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        report += f"{student:10} | Avg: {avg:6.2f} | Grade: {grade} | Status: {status}\n"
        if avg >= passing_avg:
            passed_students += 1
        else:
            failed_students += 1

    report += f"{'='*32}\nTotal Students : {total_students}\nPassed         : {passed_students}\nFailed         : {failed_students}"

    print(report)


# Task 1: Process the Scores
students = {"Ajith": [100,90,50,70,80], "Ram": [80,40,60,50,60], "John": [90,85,80,75,95]}
Students_with_averages = process_scores(students)
print("Task 1: ", Students_with_averages)

# Task 2: Classify the Grades
Students_with_grades = classify_grades(Students_with_averages)
print("Task 2: ", Students_with_grades)

#Task 3 — Generate the Report
generate_report(Students_with_grades, 70)