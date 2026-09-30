from constants import GRADE_SCALE

def validate_subject_name(name):
    if not isinstance(name, str):
        raise ValueError("Subject name must be text")
    name = name.strip()
    if len(name) == 0:
        raise ValueError("Subject name cannot be empty")
    if len(name) > 50:
        raise ValueError("Subject name too long (max 50 characters)")
    return name

def validate_grade(grade):
    if not isinstance(grade, str):
        raise ValueError("Grade must be a letter")
    grade = grade.strip().upper()
    if grade not in GRADE_SCALE:
        raise ValueError(f"Invalid grade. Choose from: {', '.join(GRADE_SCALE.keys())}")
    return grade

def validate_credits(credits):
    if not isinstance(credits, int):
        raise ValueError("Credits must be a whole number")
    if credits < 1 or credits > 5:
        raise ValueError("Credits must be between 1 and 5")