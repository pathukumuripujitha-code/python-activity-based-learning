
# University Scholarship Allocation System

students = [
    {"name": "Ravi", "marks": [85, 90, 80],
     "attendance": 92, "income": 150000},
    {"name": "Priya", "marks": [90, 95, 88],
     "attendance": 95, "income": 120000},
    {"name": "Kiran", "marks": [70, 75, 65],
     "attendance": 85, "income": 200000},
    {"name": "Anu", "marks": [90, 95, 88],
     "attendance": 95, "income": 100000},
    {"name": "Sita", "marks": [80, 82, 78],
     "attendance": 78, "income": 90000}
]

min_aggregate = 75
min_subject = 60
min_attendance = 80
max_income = 180000

eligible = []
rejected = []

for student in students:
    marks = student["marks"]
    aggregate = sum(marks) / len(marks)
    reasons = []

    if aggregate < min_aggregate:
        reasons.append("Low aggregate")
    if min(marks) < min_subject:
        reasons.append("Low subject marks")
    if student["attendance"] < min_attendance:
        reasons.append("Low attendance")
    if student["income"] > max_income:
        reasons.append("High family income")

    student["aggregate"] = aggregate

    if not reasons:
        eligible.append(student)
    else:
        rejected.append((student["name"], reasons))

# Rank: aggregate descending, income ascending,
# attendance descending, then name alphabetically
eligible.sort(key=lambda s: (
    -s["aggregate"], s["income"],
    -s["attendance"], s["name"]
))

print("UNIVERSITY SCHOLARSHIP RESULTS")
print("-" * 40)
print("\nEligible Students (Ranked):")

for rank, student in enumerate(eligible, start=1):
    print(rank, student["name"],
          "Aggregate:", round(student["aggregate"], 2),
          "Income:", student["income"],
          "Attendance:", student["attendance"])

print("\nRejected Applicants:")
for name, reasons in rejected:
    print(name, "-", ", ".join(reasons))

print("\nTotal Eligible:", len(eligible))
print("Total Rejected:", len(rejected))
