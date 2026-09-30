from storage import load_data, save_data
from validators import validate_subject_name, validate_grade, validate_credits

def add_subject(name, grade, credits):
    name = validate_subject_name(name)
    grade = validate_grade(grade)
    validate_credits(credits)

    data = load_data()
    for s in data["subjects"]:
        if s["name"].upper() == name.upper():
            raise ValueError(f"Subject '{name}' already exists. Use update instead.")

    data["subjects"].append({
        "name": name,
        "grade": grade,
        "credits": credits
    })
    save_data(data)

def update_subject(name, grade, credits):
    name = validate_subject_name(name)
    grade = validate_grade(grade)
    validate_credits(credits)

    data = load_data()
    for s in data["subjects"]:
        if s["name"].upper() == name.upper():
            s["grade"] = grade
            s["credits"] = credits
            save_data(data)
            return
    raise ValueError(f"Subject '{name}' not found.")

def delete_subject(name):
    data = load_data()
    original_len = len(data["subjects"])
    data["subjects"] = [s for s in data["subjects"] if s["name"].upper() != name.strip().upper()]
    if len(data["subjects"]) == original_len:
        raise ValueError(f"Subject '{name}' not found.")
    save_data(data)

def get_all_subjects():
    return load_data()["subjects"]