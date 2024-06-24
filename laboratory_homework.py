
if __name__ == "__main__":

    studyField = ["MECHANICAL_ENGINEERING", "SOFTWARE_ENGINEERING",
                  "FOOD_TECHNOLOGY", "URBANISM_ARCHITECTURE", "VETERINARY_MEDICINE"]

    class Student:
        def __init__(self, firstName, lastName, email, enrollment_date, dateOfBirth):
            self.firstName = firstName
            self.lastName = lastName
            self.email = email
            self.enrollment_date = enrollment_date
            self.dateOfBirth = dateOfBirth


    class Faculty:
        def __init__(self, name, abbreviation, students, studyField):
            self.name = name
            self.abbreviation = abbreviation
            self.students = students
            self.studyField = studyField
            self.students = students if students else []



    # 1. Create and assign a student to a faculty.

    student1 = Student("Vadim",
                       "Oala",
                       "vadimoala@gmail.com",
                       "2024-04-27",
                       "1991-12-31")

    engineering_faculty = Faculty("Engineering Faculty",
                                  "ENG",
                                  [student1],
                                  "MECHANICAL_ENGINEERING")

    # 2. Graduate a student from a faculty.
    engineering_faculty.students.remove(student1)

    # 3. Display current enrolled students (Graduates would be ignored).

    for student in engineering_faculty.students:
        print(f"{student1.firstName} {student.lastName} ({student.email})")

    # 4. Display graduates (Currently enrolled students would be ignored).

    # 5. Tell or not if a student belongs to this faculty.

    def student_belongs_to_faculty(student1, faculty):
        return student1.email in [s.email for s in faculty.students]

    print(student_belongs_to_faculty(student1, engineering_faculty))

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






