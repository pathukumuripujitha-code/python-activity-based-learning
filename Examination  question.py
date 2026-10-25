
# Examination Question Difficulty and Performance Analysis

answer_key = ["A", "B", "C", "D", "A"]
students = {
    "Student1": ["A", "B", "C", "A", "A"],
    "Student2": ["A", "C", "C", "D", "B"],
    "Student3": ["B", "B", "A", "D", "A"],
    "Student4": ["A", "B", "C", "C", "A"],
    "Student5": ["C", "A", "C", "D", "B"]
}

total_students = len(students)
total_questions = len(answer_key)
correct_counts = [0] * total_questions

print("EXAMINATION PERFORMANCE ANALYSIS")
print("-" * 40)

# Compare student answers with the key
for name, answers in students.items():
    score = 0
    for i in range(total_questions):
        if answers[i].upper() == answer_key[i]:
            score += 1
            correct_counts[i] += 1
    print(name, "Score:", score, "/", total_questions)

print("\nQUESTION-WISE ANALYSIS")
missed_questions = []

# Calculate success rates and classify questions
for i in range(total_questions):
    success_rate = (correct_counts[i] / total_students) * 100
    missed = total_students - correct_counts[i]

    if success_rate >= 80:
        category = "Easy"
    elif success_rate >= 50:
        category = "Moderate"
    else:
        category = "Difficult"

    print("Question", i + 1)
    print("Success Rate:", round(success_rate, 2), "%")
    print("Incorrect Answers:", missed)
    print("Classification:", category)

    if missed >= 3:
        missed_questions.append(i + 1)

# Identify frequently missed questions
print("\nFREQUENTLY MISSED QUESTIONS:")
if missed_questions:
    print("Questions:", missed_questions)
else:
    print("No questions were frequently missed.")

# Find the most difficult question
lowest_correct = min(correct_counts)
hardest = [i + 1 for i, count in enumerate(correct_counts)
           if count == lowest_correct]

print("Most Difficult Question(s):", hardest)
print("Analysis Completed Successfully.")
