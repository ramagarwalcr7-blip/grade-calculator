from grades import add_subject, update_subject, delete_subject
from reports import show_all_grades, show_gpa_summary

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def menu_add():
    print("\n-- Add Subject --")
    name = input("Subject name: ").strip()
    grade = input("Grade (S/A/B/C/D/E/F): ").strip().upper()
    credits = get_int("Credits (1-5): ")
    try:
        add_subject(name, grade, credits)
        print(f"\n'{name}' added successfully.")
    except ValueError as e:
        print(f"\nError: {e}")

def menu_update():
    print("\n-- Update Subject --")
    name = input("Subject name to update: ").strip()
    grade = input("New grade (S/A/B/C/D/E/F): ").strip().upper()
    credits = get_int("New credits (1-5): ")
    try:
        update_subject(name, grade, credits)
        print(f"\n'{name}' updated successfully.")
    except ValueError as e:
        print(f"\nError: {e}")

def menu_delete():
    print("\n-- Delete Subject --")
    name = input("Subject name to delete: ").strip()
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        try:
            delete_subject(name)
            print(f"\n'{name}' deleted.")
        except ValueError as e:
            print(f"\nError: {e}")
    else:
        print("Cancelled.")

def main():
    print("=" * 40)
    print("  Student Grade Calculator")
    print("=" * 40)

    while True:
        print("\n1. View all grades")
        print("2. Add subject")
        print("3. Update subject")
        print("4. Delete subject")
        print("5. View GPA summary")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            show_all_grades()
        elif choice == "2":
            menu_add()
        elif choice == "3":
            menu_update()
        elif choice == "4":
            menu_delete()
        elif choice == "5":
            show_gpa_summary()
        elif choice == "6":
            print("\nGoodbye.\n")
            break
        else:
            print("Invalid choice. Enter 1-6.")

if __name__ == "__main__":
    main()