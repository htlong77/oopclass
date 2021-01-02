"""
Education  related!!!
"""
try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")
from vietnamese import *
import pandas

class Semester:
    """Semester related"""
    def __init__(self, id, description=None):
        """Initialize new student with his/her id."""
        self.id = id
        self.description = description
        self.courses = []

    def add_course(self, course):
        """Add course."""
        self.courses.append(course)

    def to_xml(self):
        """To xml"""
        root = etree.Element("semester", id=self.id, description=self.description)
        for course in self.courses:
            course_child = etree.SubElement(root, 'course')
            course_child.set("code", course.code)
#            if len(course.students) > 0:
            if len(course.student_ids) > 0:
              ids_child = etree.SubElement(course_child, 'ids')
#              ids = []
#              for student in course.students:
#                ids.append(student.student_id)
#              ids_child.text = ','.join(ids)
              ids_child.text = ','.join(course.student_ids)
        return etree.tostring(root, encoding="UTF-8", pretty_print=True).decode()

    def __str__(self):
        return f"""Semester ID: {self.id}
Description: {self.description}"""

class Student:
    """Student related"""

    def __init__(self, student_id):
        """Initialize new student with his/her id."""
        self.student_id = student_id

    def set_name(self, name):
        """Set name for the student."""
        self.name = VnFullName(name)

    def __str__(self):
        return f"{self.student_id}"

class Course:
    """Course managed!!!"""
    def __init__(self, code):
#subject, num_of_credits, day_of_week, course_hours, course_room
        """Initialize the course with a course code."""
        self.code = code
#        self.students = []
        self.student_ids = []
        
    def set_subject(self, subject):
        """Set the subject of the course."""
        self.subject = subject

    def set_num_of_credits(self, num_of_credits):
        """Set the number of credits of the course."""
        self.num_of_credits = num_of_credits

    def add_granted_room(self, granted_room):
        """Add a granted room to the course."""

#    def load_students(self, filename):
#        """Load student informations from 'filename'."""
#        ifile = open(filename, 'r')
#        data_lines = ifile.readlines()[1:] # The first line is the header row
#        for line in data_lines:
#            # remove the newline character '\n' at the end of each line
#            line = line[:-1]
#            name, date_of_birth, student_id = line.split(',')[1:]
#            new_student = Student(student_id)
#            new_student.set_name(name)
#            self.students.append(new_student)
#        ifile.close()

    def load_enrolled_students(self, filename):
        """Load enrolled students from 'filename'."""
        print(f"Load enrolled students from '{filename}'")
        df = pandas.read_csv(filename, parse_dates=['Timestamp'])
        print(f"Number of students read: {len(df['Mã sinh viên'])}")
        ids = []
        for id in df.index:
          student_id = str(df['Mã sinh viên'][id])
          if ids.count(student_id) == 0:
            ids.append(student_id)
        self.student_ids = ids

#    def sort_students_by_name(self):
#        """Sort students by name."""
#        lenlist = len(self.students)
#        for i in range(lenlist-1):
#            for j in range(i+1, lenlist):
#                iname = self.students[i].name
#                jname = self.students[j].name
#                if iname.compare(jname) > 0:
#                    self.students[i], self.students[j] = self.students[j], self.students[i]

#    def print_names(self):
#        """Print name of students."""
#        for student in self.students:
#            print(f"{student.name}")

    def print_ids(self):
        """Print ID of students."""
        for student in self.students:
            print(f"{student}")

    def __str__(self):
      if hasattr(self, 'subject'):
        return f"{self.code}:{self.subject}"
      else:
        return f"{self.code}"

def test_Semester():
    "Test 'Semester' class!!!"
    print("Testing 'Semester' class...")
    hk12021 = Semester("hk12021", "Học kỳ I, năm học 2020-2021")
    print(hk12021)
    print("All passed!!!")

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
#    phy3176.load_students('old_load.csv')
#    print("Before sorting names.")
#    phy3176.print_names()
#    phy3176.sort_students_by_name()
#    print("After sorting names.")
#    phy3176.print_names()

def test():
    """Test command goes here!!!"""
    test_Course()
    test_Semester()
        
if __name__ == "__main__":
    test()
    
