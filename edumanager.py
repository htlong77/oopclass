"""CLI for Education Manager"""
course_code = None
def display_infos():
    print(f"""Current course: {course_code}""")
    
def display_menu():
    print("""1. New course
2. 
3.
0. Quit!!!
Your choice: """, end = "" )

if __name__ == "__main__":
    """Main program"""
    choice = 1
    print('why')
    while choice != 0:
        print("ha ha")
        display_infos()
        display_menu()
        choice = int(input())
        
