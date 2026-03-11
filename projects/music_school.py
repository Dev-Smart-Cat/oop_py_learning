class MusicSchool:

    students = {"Gino": [15, "653-235-345", ["Piano", "Guitar"]],
                "Tatiana": [28, "555-765-452", ["Cello"]],
                "Eric": [12, "583-356-223", ["Singing"]]}
    
    def __init__(self, working_hours, revenue):
        # These are the instance attributes/parameters
        self.working_hours = working_hours
        self.revenue = revenue

    # This is a METHOD to print the student data
    def print_student_data(self):
        for name in MusicSchool.students:
            self.print_student(name)

    # This is a METHOD to print a student
    def print_student(self, name):
        data = MusicSchool.students[name]
        print("Student: " + name + " who is " + str(data[0]) + " years old and is taking " + str(data[2]))

    # This is a METHOD to add a student
    def add_student(self, name, data):
        MusicSchool.students[name] = data

# Create a instance to add the working hours and the revenue
headquaters = MusicSchool(8, 15000)
# Print the student data
headquaters.print_student_data()
# Print the data of one student
headquaters.print_student("Gino")
# Add a student
headquaters.add_student("Jack", [60, "562-234-234", ["Piano"]])

    