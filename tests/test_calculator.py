import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import calculator

def test_grade_to_points():
    assert calculator.grade_to_points("S") == 10
    assert calculator.grade_to_points("A") == 9
    assert calculator.grade_to_points("F") == 0

def test_calculate_gpa():
    subjects = [
        {"grade": "A", "credits": 4},
        {"grade": "B", "credits": 3},
    ]
    assert calculator.calculate_gpa(subjects) == 8.57

def test_is_pass():
    assert calculator.is_pass("E") == True
    assert calculator.is_pass("F") == False
    assert calculator.is_pass("S") == True

def test_get_status():
    assert calculator.get_status("A") == "PASS"
    assert calculator.get_status("F") == "FAIL"

def test_credits_at_risk():
    subjects = [
        {"grade": "A", "credits": 4},
        {"grade": "F", "credits": 3},
        {"grade": "F", "credits": 2},
    ]
    assert calculator.credits_at_risk(subjects) == 5

if __name__ == "__main__":
    passed = 0
    failed = 0
    tests = [test_grade_to_points, test_calculate_gpa, test_is_pass, test_get_status, test_credits_at_risk]
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
            passed += 1
        except AssertionError:
            print(f"FAIL: {test.__name__}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")    
    