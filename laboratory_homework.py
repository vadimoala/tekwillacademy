
if __name__ == "__main__":

    studyField = ["MECHANICAL_ENGINEERING", "SOFTWARE_ENGINEERING",
                  "FOOD_TECHNOLOGY", "URBANISM_ARCHITECTURE", "VETERINARY_MEDICINE"]
    class Student:
        def __init__(self, firstName, lastName, email, enrollmentDate, dateOfBirth):
            self.firstName = firstName
            self.lastName = lastName
            self.email = email
            self.enrollmentDate = enrollmentDate
            self.dateOfBirth = dateOfBirth

    class Faculty:
        def __init__(self, name, abbreviation, students, studyField):
            self.name = name
            self.abbreviation = abbreviation
            self.students = students
            self.studyField = studyField

    # 1. Create and assign a student to a faculty.
    student1 = Student("Vadim",
                       "Oala",
                       "vadimoala@gmail.com",
                       "2024-04-27",
                       "1991-12-31")

    faculty1 = Faculty("Engineering Faculty",
                        "ENG",
                        [student1],
                        "MECHANICAL_ENGINEERING")

    print(f"Student: {student1.firstName} {student1.lastName}")
    print(f"Enrollment Date: {student1.enrollmentDate}")
    print(f"Faculty: {faculty1.name} ({faculty1.abbreviation})")
    print(f"Study Field: {faculty1.studyField}")

    # 2. Graduate a student from a faculty.

    faculty1.students.remove(student1)
    print(f"{student1.firstName} {student1.lastName} has graduated from {faculty1.name}.")

    # 3. Display current enrolled students (Graduates would be ignored).

    print("Currently enrolled students:")
    for student in faculty1.students:
        print(f"{student.firstName} {student.lastName}")

    # 4. Display graduates (Currently enrolled students would be ignored).

    print("Graduated students:")
    for student in faculty1.students:
        if student.has_graduated:
            print(f"{student.firstName} {student.lastName}")


    # 5. Tell or not if a student belongs to this faculty.

    def student_belongs_to_faculty(student1, faculty):
        return student1.email in [s.email for s in faculty.students]

    print(student_belongs_to_faculty(student1, faculty1))

    # General operations:
    # 1.Create a new faculty.

    computer_designer = Faculty("Computer Designer",
                                "CD",
                                [],
                                "SOFTWARE_ENGINEERING")

    # 2. Search what faculty a student belongs to by a unique identifier
    # (for example by email or a unique ID).

    def identifier(identifier):
        for faculty in studyField:
            for student in faculty.students:
                if student.email == identifier:
                    return faculty
        return None

    # 3. Display University faculties.

    # 4. Display all faculties belonging to a field. (Ex. FOOD_TECHNOLOGY)








