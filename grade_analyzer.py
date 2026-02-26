# ======================================
# Student Grade Analyzer
# ======================================

# Task 1 — Process the Scores
def process_scores(students):
    """
    Accepts dictionary {name: [scores]}
    Returns {name: average_score} rounded to 2 decimals
    """
    averages = {}
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages


# Task 2 — Classify the Grades
def classify_grades(averages):
    """
    Accepts {name: average}
    Returns {name: (average, grade)}
    """

    # Grade thresholds (defined locally — NOT global)
    A_THRESHOLD = 90
    B_THRESHOLD = 75
    C_THRESHOLD = 60

    classified = {}

    for name, avg in averages.items():
        if avg >= A_THRESHOLD:
            grade = "A"
        elif avg >= B_THRESHOLD:
            grade = "B"
        elif avg >= C_THRESHOLD:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


# Task 3 — Generate the Report
def generate_report(classified, passing_avg=70):
    """
    Prints formatted report
    Returns number of students who passed
    """

    print("===== Student Grade Report =====")

    total_students = len(classified)
    passed = 0
    failed = 0

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"

        if status == "PASS":
            passed += 1
        else:
            failed += 1

        print(f"{name:<10} | Avg: {avg:6.2f} | Grade: {grade} | Status: {status}")

    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed


# ======================================
# Main Block
# ======================================
if __name__ == "__main__":

    students = {
        "Alice": [85, 90, 88, 82],
        "Bob": [60, 65, 63, 62],
        "Clara": [95, 98, 94, 98]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    total_passed = generate_report(classified)