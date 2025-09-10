# Student Grades Program using Dictionary

students = {}  # Empty dictionary to store student grades

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Print All Grades")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print(f"{name} added with grade {grade}.")
        
    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print("Student not found!")
            
    elif choice == 3:
        print("\n--- All Student Grades ---")
        if len(students) == 0:
            print("No students added yet.")
        else:
            for name, grade in students.items():
                print(name, ":", grade)
                
    elif choice == 4:
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice! Please select 1-4.")

