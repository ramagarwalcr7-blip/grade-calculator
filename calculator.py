from constants import GRADE_SCALE, PASS_GPA

def grade_to_points(grade):
    return GRADE_SCALE.get(grade.upper(), 0)

def calculate_gpa(subjects):
    if not subjects:
        return 0.0
    total_points = 0
    total_credits = 0
    for s in subjects:
        total_points += grade_to_points(s["grade"]) * s["credits"]
        total_credits += s["credits"]
    if total_credits == 0:
        return 0.0
    return round(total_points / total_credits, 2)

def calculate_percentage(grade):
    points = grade_to_points(grade)
    return round((points / 10) * 100, 2)

def is_pass(grade):
    return grade_to_points(grade) >= PASS_GPA

def get_status(grade):
    if is_pass(grade):
        return "PASS"
    return "FAIL"

def credits_at_risk(subjects):
    return sum(s["credits"] for s in subjects if not is_pass(s["grade"]))