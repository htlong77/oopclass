"""CLI for Education Manager"""
from education import *

semester = None
course = None

def change_semester_id():
  """Change semester id."""
  if semester is not None:
    id = input("New ID? ")
    if id != "":
      semester.id = id

def change_semester_description():
  """Change semester description."""
  if semester is not None:
    description = input("Description? ")
    if description != "":
      semester.description = description
      
def new_semester():
  """Create new semester."""
  id = input("New semester ID? ")
  description = input("Description? ").strip()
  return Semester(id, description)
  
def load_semester():
  """Load an existing semester."""
  filename = input('Load from file ("semester.xml")? ')
  if filename == "":
    filename = "semester.xml"
  root = etree.parse(filename).getroot()
#  print(etree.tostring(root, encoding="UTF-8", pretty_print=True).decode())
  id = root.get("id")
  description = root.get("description")
  tmp = Semester(id, description)
  for child in root:
    if child.tag == "course":
      code = child.attrib['code']
      tmp.add_course(Course(code))
  return tmp

def add_course():
  """Add course."""
  code = input("New course code? ")
  if semester is not None:
    semester.add_course(Course(code.upper()))
  
def get_course():
  """Change to course."""
  num_of_courses = len(semester.courses)
  if num_of_courses > 1:
    index = int(input(f"Course number [1-{num_of_courses}]? "))
    if 1 <= index <= num_of_courses:
      return semester.courses[index-1]
  elif num_of_courses == 1:
    return semester.courses[0]
  else: return None
    
def load_enrolled_students():
  """Load enrolled students."""
  csvfile = input("Csv file to load from (enrolled_students.csv)? ")
  if csvfile == "":
    csvfile = "enrolled_students.csv"
  if course is not None:
    course.load_enrolled_students(csvfile)

def list_courses():
  """List course."""
  if semester is not None:
    index = 0
    num_of_courses = len(semester.courses)
    width = len(str(num_of_courses))
    for course in semester.courses:
      index += 1
      print(f"{index:{width}}/{num_of_courses:{width}}:{course}")
  
def save_to_disk():
  filename = input('Save to file ("semester.xml")? ')
  if filename == "":
    filename = "semester.xml"
  ofile = open(filename, 'w')
  ofile.write(semester.to_xml())
  ofile.close()
  
def display_infos():
  if semester is not None:
    print(f"""{semester}
Current course: {course}""")
  else:
    print("""Semester ID:
Description: 
Current course:""")
    
    
def display_menu():
    print("""1. Load Semester.
2. List courses.
3. Add course.
4. Change Semester Description.
5. Change Semester ID.
6. Save to disk.
7. Change to course.
8. New Semester.
9. Load enrolled students.
0. Quit!!!
============
Your choice: """, end = "" )

if __name__ == "__main__":
    """Main program"""
    import sys
    choice = 1
    while choice != 0:
        display_infos()
        display_menu()
        try:
          choice = int(input())
        except:
          print('Please input a number!!!');sys.exit()
        if choice == 1:
          semester = load_semester()
        elif choice == 2:
          list_courses() 
        elif choice == 3:
          course = add_course() 
        elif choice == 4:
          change_semester_description()
        elif choice == 5:
          change_semester_id()
        elif choice == 6:
          save_to_disk()
        elif choice == 7:
          course = get_course()
        elif choice == 8:
          semester = new_semester()
        elif choice == 9:
          semester = load_enrolled_students()
        else:
          pass
        
