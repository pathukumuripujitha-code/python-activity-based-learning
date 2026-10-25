
# University Examination Result Moderation

students = {
    "Ravi": [28, 32, 35],
    "Priya": [22, 25, 30],
    "Kiran": [38, 40, 45],
    "Anu": [18, 27, 33]
}

max_marks = [100, 100, 100]
pass_mark = 30
moderation_limit = 5

print("UNIVERSITY RESULT MODERATION REPORT")
print("-" * 50)

for name, marks in students.items():
    original_total = sum(marks)
    moderated_marks = []
    moderation_used = 0

    for i in range(len(marks)):
        mark = marks[i]
        maximum = max_marks[i]

        if mark < pass_mark and moderation_used < moderation_limit:
            required = pass_mark - mark
            grace = min(required, moderation_limit - moderation_used)
            mark += grace
            moderation_used += grace

        mark = min(mark, maximum)
        moderated_marks.append(mark)

    moderated_total = sum(moderated_marks)
    original_result = all(m >= pass_mark for m in marks)
    moderated_result = all(m >= pass_mark for m in moderated_marks)

    print("\nStudent:", name)
    print("Original Marks:", marks)
    print("Moderated Marks:", moderated_marks)
    print("Original Total:", original_total)
    print("Moderated Total:", moderated_total)
    print("Marks Increased:", moderated_total - original_total)

    if original_result:
        print("Original Result: PASS")
    else:
        print("Original Result: FAIL")

    if moderated_result:
        print("Moderated Result: PASS")
    else:
        print("Moderated Result: FAIL")

    print("Moderation Marks Used:", moderation_used)
    print("-" * 50)
