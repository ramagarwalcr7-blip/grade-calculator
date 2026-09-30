from calculator import calculate_gpa, calculate_percentage, get_status, credits_at_risk
from grades import get_all_subjects

def show_all_grades():
    subjects = get_all_subjects()
    if not subjects:
        print("\nNo subjects added yet.\n")
        return

    print("\n" + "=" * 55)
    print(f"{'SUBJECT':<20} {'GRADE':>6} {'CREDITS':>8} {'STATUS':>10}")
    print("=" * 55)

    for s in subjects:
        status = get_status(s["grade"])
        print(f"{s['name']:<20} {s['grade']:>6} {s['credits']:>8} {status:>10}")

    print("=" * 55)
    gpa = calculate_gpa(subjects)
    at_risk = credits_at_risk(subjects)
    print(f"\nCurrent GPA:     {gpa}")
    print(f"Credits at risk: {at_risk}")
    print()

def show_gpa_summary():
    subjects = get_all_subjects()
    if not subjects:
        print("\nNo subjects added yet.\n")
        return

    gpa = calculate_gpa(subjects)
    at_risk = credits_at_risk(subjects)
    total_credits = sum(s["credits"] for s in subjects)

    print("\n--- GPA Summary ---")
    print(f"Total subjects:   {len(subjects)}")
    print(f"Total credits:    {total_credits}")
    print(f"GPA:              {gpa} / 10")
    print(f"Credits at risk:  {at_risk}")

    if gpa >= 8.5:
        print("Performance:      Excellent")
    elif gpa >= 7.0:
        print("Performance:      Good")
    elif gpa >= 5.0:
        print("Performance:      Average")
    else:
        print("Performance:      Poor — multiple subjects at risk")
    print()