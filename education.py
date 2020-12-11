"""
Education  related!!!
"""
class Class:
    """Class managed!!!"""
    def __init__(self, code):
#subject, num_of_credits, day_of_week, class_hours, class_room
        """Initialize the class with a class code."""
        self.code = code
    def set_subject(self, subject):
        """Set the subject of the class."""
        self.subject = subject

    def set_num_of_credits(self, num_of_credits):
        """Set the number of credits of the class."""
        self.num_of_credits = num_of_credits

    def add_granted_room(self, granted_room):
        """Add a granted room to the class."""
        

def test():
    """Test command goes here!!!"""
    phy3176 = Class("PHY3176")
    phy3176.set_subject("Cấu trúc và phản ứng hạt nhân")
    phy3176.set_num_of_credits(3)
    #
    print("Testing...")
    assert(phy3176.code == 'PHY3176')
    assert(phy3176.subject == "Cấu trúc và phản ứng hạt nhân")
    assert(phy3176.num_of_credits == 3)
    print("All passed. Done!!!")
        
if __name__ == "__main__":
    test()
