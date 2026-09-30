Grade Calculator

a command line tool for VIT students to track their grades and calculate GPA. it uses VIT's own grading scale so the GPA it shows is accurate for VIT only. made in python.

Features
add your subjects with grade and credits
calculates GPA automatically using VIT grading scale
shows pass or fail status for each subject
shows how many credits are at risk (credits of subjects you failed)
you can add, update and delete subjects
checks if input is correct before saving
data is saved in a json file so it doesnt disappear
Grading Scale
Grade	Points
S	10
A	9
B	8
C	7
D	6
E	5
F	0

minimum passing grade is E (5 points). anything below that is fail.

How to Run

python main.py

menu will look like this -

View all grades
Add subject
Update subject
Delete subject
View GPA summary
Exit

some rules for input -

subject name cannot be empty
grade must be one of these only - S, A, B, C, D, E, F
credits must be a whole number between 1 and 5
Project Structure

i divided into multiple files so code is more organised and easier to read -

grade-calculator/
├── main.py # main file, run this only
├── constants.py # grading scale and fixed values stored here
├── calculator.py # GPA calculation and pass fail logic
├── validators.py # checks if name, grade, credits are correct
├── storage.py # saves and loads grades.json file
├── grades.py # add, update, delete subjects
├── reports.py # shows grade table and GPA summary nicely
├── data/
│ └── grades.json # all subject data saved here
└── tests/
└── test_calculator.py

Tests

python tests\test_calculator.py

all 5 tests are passing currently

Repository

github.com/ramagarwalcr7-blip/grade-calculator