"""CLI for Education Manager"""
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

database = None
def display_infos():
    print(f"""Current database: {database}""")
    
def display_menu():
    print("""1. New database
2. 
3.
0. Quit!!!
Your choice: """, end = "" )

if __name__ == "__main__":
    """Main program"""
    choice = 1
    while choice != 0:
        display_infos()
        display_menu()
        choice = int(input())
        
