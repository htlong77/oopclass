"""
Education  related!!!
"""
from vietnamese import *
class Student:
    """Student related"""

    def __init__(self, student_id):
        """Initialize new student with his/her id."""
        self.student_id = student_id

    def set_name(self, name):
        """Set name for the student."""
        self.name = VnFullName(name)

class Course:
    """Course managed!!!"""
    def __init__(self, code):
#subject, num_of_credits, day_of_week, course_hours, course_room
        """Initialize the course with a course code."""
        self.code = code
        self.students = []
        
    def set_subject(self, subject):
        """Set the subject of the course."""
        self.subject = subject

    def set_num_of_credits(self, num_of_credits):
        """Set the number of credits of the course."""
        self.num_of_credits = num_of_credits

    def add_granted_room(self, granted_room):
        """Add a granted room to the course."""

    def load_students(self, filename):
        """Load student informations from 'filename'."""
        ifile = open(filename, 'r')
        data_lines = ifile.readlines()[1:] # The first line is the header row
        for line in data_lines:
            # remove the newline character '\n' at the end of each line
            line = line[:-1]
            name, date_of_birth, student_id = line.split(',')[1:]
            new_student = Student(student_id)
            new_student.set_name(name)
            self.students.append(new_student)
        ifile.close()

    def sort_students_by_name(self):
        """Sort students by name."""
        lenlist = len(self.students)
        for i in range(lenlist-1):
            for j in range(i+1, lenlist):
                iname = self.students[i].name
                jname = self.students[j].name
                if iname.compare(jname) > 0:
                    self.students[i], self.students[j] = self.students[j], self.students[i]

    def print_names(self):
        """Print name of students."""
        for student in self.students:
            print(f"{student.name}")

def test_Course():
    "Test 'Course' class!!!"
    print("Testing 'Course' class...")
    phy3176 = Course("PHY3176")
    phy3176.set_subject("Cấu trúc và phản ứng hạt nhân")
    phy3176.set_num_of_credits(3)
    #
    assert(phy3176.code == 'PHY3176')
    assert(phy3176.subject == "Cấu trúc và phản ứng hạt nhân")
    assert(phy3176.num_of_credits == 3)
    print("All passed. Done!!!")
    phy3176.load_students('phy3176_20202021__1st_semester.csv')
    print("Before sorting names.")
    phy3176.print_names()
    phy3176.sort_students_by_name()
    print("After sorting names.")
    phy3176.print_names()

def test():
    """Test command goes here!!!"""
    test_Course()
        
if __name__ == "__main__":
    test()
