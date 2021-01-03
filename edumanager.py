"""CLI for Education Manager"""
from education import *

semester = None
course = None
student_database_file = None
basic_information_df = None

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
  
def load_semester_from(filename):
  """Load an existing semester."""
  root = etree.parse(filename).getroot()
  id = root.get("id")
  description = root.get("description")
  tmp = Semester(id, description)
  for child in root:
    if child.tag == "course":
      code = child.attrib['code']
      course_tmp = Course(code)
      for child_of_course in child:
        if child_of_course.tag == "ids":
          ids = child_of_course.text.split(',')
          course_tmp.student_ids = ids
      tmp.add_course(course_tmp)
  return tmp

def load_semester():
  """Load an existing semester."""
  filename = input('Load from file ("semester.xml")? ')
  if filename == "":
    filename = "semester.xml"
  return load_semester_from(filename)

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
      print(f"{index:{width}}/{num_of_courses:{width}}: {course} ({len(course.student_ids)} students).")
  
def save_to_disk():
  filename = input('Save to file ("semester.xml")? ')
  if filename == "":
    filename = "semester.xml"
  ofile = open(filename, 'w')
  ofile.write(semester.to_xml())
  ofile.close()
  
def save_student_database_to_csv_file():
  """Save student database to csv file (Ascending order by student's ID)."""
  default_file = student_database_file
#  default_file = 'test.csv'
  csvfile = input(f"Csv file to save to ({default_file})? ")
  if csvfile == "":
    csvfile = default_file
  print(f"Save to file '{csvfile}'")
  #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
  basic_information_df.sort_values(by='Mã sinh viên', inplace=True)
  # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
  basic_information_df.to_csv(csvfile, index=False)

def basic_informations_from_csv_file(csvfile):
  """Load basic information from csv file 'filename'."""
  df = pandas.read_csv(csvfile, parse_dates=['Timestamp'])
  basic_info_df = df.loc[:,['Mã sinh viên', 'Họ và tên sinh viên', 'Ngày tháng năm sinh', 'Timestamp']]
  return basic_info_df

def load_and_append_student_database_from_csv_file():
  """Load student database from csv file."""
  csvfile = input(f"Csv file to load from ({student_database_file})? ")
  if csvfile == "":
    csvfile = student_database_file
  print(f"Loading from file '{csvfile}'")
  tmp = basic_informations_from_csv_file(csvfile)
  print(f"{len(tmp['Mã sinh viên'])} students.")
  basic_information_df_tmp = basic_information_df
  for index in tmp.index:
    student_id = tmp.loc[index]['Mã sinh viên']
    # check if student_id exists in database
    if basic_information_df_tmp[basic_information_df_tmp['Mã sinh viên']==student_id].size == 0:
      # append student's data to the database
      student = tmp.loc[index]
      basic_information_df_tmp = basic_information_df_tmp.append(student)
  return basic_information_df_tmp

def display_infos():
  if semester is not None:
    print(f"""{semester}
    Current course: {course} ({len(course.student_ids)} students).
    Student database: '{student_database_file}' ({len(basic_information_df['Mã sinh viên'])} students).""")
  else:
    print("""Semester ID:
Description: 
Current course:
Students database:""")
    
    
def display_menu():
    print("""1. Load Semester.
2. List courses.
3. Add course.
4. Change Semester Description.
5. Change Semester ID.
6. Save to disk.
7. Change to course.
8. New Semester.
9. Load enrolled students for current course.
10. Load student informations from csv file (then append to database).
11. Save student database to csv file.
0. Quit!!!
============
Your choice: """, end = "" )

if __name__ == "__main__":
    """Main program"""
    import sys
    choice = 1
    filename = "semester.xml"
    semester = load_semester_from(filename)
    student_database_file = "students.csv"
    basic_information_df = basic_informations_from_csv_file(student_database_file)
    if len(semester.courses) > 0: course = semester.courses[0]
    while choice != 0:
        display_infos()
        display_menu()
        try:
          choice = int(input())
        except:
          print('Please input a number!!!');sys.exit()
        if choice == 1:
          semester = load_semester()
          if len(semester.courses) > 0: course = semester.courses[0]
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
          load_enrolled_students()
        elif choice == 10:
          basic_information_df = load_and_append_student_database_from_csv_file()
        elif choice == 11:
          save_student_database_to_csv_file()
        else:
          pass
        
