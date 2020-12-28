"""CLI for Education Manager"""
from education import *

semester = None

def new_semester():
  """Create new semester."""
  id = input("New semester ID? ")
  description = input("Description? ").strip()
  return Semester(id, description)
  
def load_semester():
  """Load an existing semester."""
  filename = input('Load from file ("test.xml")? ')
  if filename == "":
    filename = "test.xml"
  root = etree.parse(filename).getroot()
  print(etree.tostring(root, encoding="UTF-8", pretty_print=True).decode())
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
  
def save_to_disk():
  filename = input('Save to file ("test.xml")? ')
  if filename == "":
    filename = "test.xml"
  ofile = open(filename, 'w')
  ofile.write(semester.to_xml())
  ofile.close()
  
def display_infos():
    print(semester)
    
def display_menu():
    print("""1. New Semester
2. Save to disk
3. Add course.
4. Load Semester.
0. Quit!!!
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
          semester = new_semester()
        elif choice == 2:
          save_to_disk()
        elif choice == 3:
          add_course() 
        elif choice == 4:
          semester = load_semester()
        else:
          pass
        
