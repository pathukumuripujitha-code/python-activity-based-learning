
# Student Timetable Conflict Detection

courses = [
    ("Python", "Monday", "09:00", "10:00", "R101"),
    ("Maths", "Monday", "09:30", "10:30", "R102"),
    ("AI", "Tuesday", "10:00", "11:00", "R101"),
    ("English", "Monday", "11:00", "12:00", "R101")
]

unavailable_rooms = ["R102", "R105"]

def to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def detect_conflicts(schedule):
    conflicts = []
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            c1, c2 = schedule[i], schedule[j]
            if c1[1] == c2[1]:
                start1, end1 = to_minutes(c1[2]), to_minutes(c1[3])
                start2, end2 = to_minutes(c2[2]), to_minutes(c2[3])
                if start1 < end2 and start2 < end1:
                    conflicts.append((c1[0], c2[0]))
    return conflicts

def check_rooms(schedule):
    for course in schedule:
        if course[4] in unavailable_rooms:
            print(course[0], "uses unavailable room", course[4])

def validate_timetable(schedule):
    conflicts = detect_conflicts(schedule)
    if conflicts:
        print("Schedule conflicts detected:")
        for first, second in conflicts:
            print(first, "overlaps with", second)
    else:
        print("No time conflicts found.")
    check_rooms(schedule)

# String representation of a course
course_string = "Physics,Tuesday,12:00,13:00,R103"
course_data = tuple(course_string.split(","))

# Add a proposed course
proposed_schedule = courses + [course_data]

print("Student Timetable Validation")
validate_timetable(proposed_schedule)
