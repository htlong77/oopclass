"""
Vietnamese related!!!
"""
vn_lowercase=" aàáảãạăằắẳẵặâầấẩẫậbcdđeèéẻẽẹêềếểễệfghiìíỉĩịjklmnoòóỏõọôồốổỗộơờớởỡợpqrstuùúủũụưừứửữựvwxyỳýỷỹỵz"
vn_uppercase=" AÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬBCDĐEÈÉẺẼẸÊỀẾỂỄỆFGHIÌÍỈĨỊJKLMNOÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢPQRSTUÙÚỦŨỤƯỪỨỬỮỰVWXYỲÝỶỸỴZ"
class VnFullName():
    def __init__(self, full_name):
        """Initialize a Vietnamese full name!!!"""
        self.full_name = full_name
        self.standardize()

    def standardize(self):
        """Standardize Vietnamese full name!!!"""
        import string
        self.full_name = string.capwords(self.full_name)

    def last_middle_first_name(self):
        """Extract last/middle/first name!!!"""
        words = self.full_name.split()
        last_name = words[0]
        first_name = words[-1]
        middle_name = " ".join(words[1:-1])
        return last_name, middle_name, first_name

    def compare(self, other_full_name):
        """Compare with other full name!!!"""
        slast, smiddle, sfirst = self.last_middle_first_name()
        olast, omiddle, ofirst = other_full_name.last_middle_first_name()
        if vntoascii(sfirst) == vntoascii(ofirst):
            if vntoascii(slast) == vntoascii(olast):
                if vntoascii(smiddle) == vntoascii(omiddle): return 0
                elif vntoascii(smiddle) > vntoascii(omiddle): return 1
                else: return -1
            elif vntoascii(slast) > vntoascii(olast): return 1
            else: return -1
        elif vntoascii(sfirst) > vntoascii(ofirst): return 1
        else: return -1

    def __str__(self):
        """Refined Vietnamese full name!!!"""
        return f"""{self.full_name}"""
        
def vntoascii(vntxt):
# Bắt chước code cung cấp tại địa chỉ 
# http://www.ddth.com/showthread.php/26725-C%C3%A1ch-s%E1%BA%AFp-x%E1%BA%BFp-t%C3%AAn-theo-th%E1%BB%A9-t%E1%BB%B1-A-B-C
    vn_ascii=""
    for n in range(len(vntxt)):
        posinlower = vn_lowercase.find(vntxt[n])
        if posinlower<0:
            posinupper = vn_uppercase.find(vntxt[n])
            if posinupper>=0:
                vn_ascii = vn_ascii+chr(100+posinupper)
            else:
                vn_ascii = vn_ascii+chr(100)
        else:
            vn_ascii = vn_ascii+chr(100+posinlower)
    return vn_ascii

def test_VnFullName():
    """Test VnFullName class!!!"""
    print("Testing VnFullName class...")
    assert(VnFullName("nguyễn duy thể") is not None)
    assert(VnFullName("   nguyễn     duy thể  ").full_name == "Nguyễn Duy Thể")
    assert(VnFullName("nguyễn duy  thể  ").last_middle_first_name() == ("Nguyễn", "Duy", "Thể"))
    assert(VnFullName("   nguyễn  hoàng  ").last_middle_first_name() == ("Nguyễn", "", "Hoàng"))
    assert(VnFullName("Vũ Trường An").compare(VnFullName("vũ trường an ")) == 0)
    assert(VnFullName("Vũ Trường An").compare(VnFullName(" nguyễn tùng anh  ")) == -1)
    print("All passed. Done!!!")
    print(VnFullName("   nguyễn   jimmy  "))
    print(VnFullName("   Trần Thị phương   anh  "))
    
def test_vn_ascii():
    """Test vn_ascii function!!!"""
    print("Testing vn_ascii function...")
    assert(vntoascii('A') == vntoascii('a'))
    assert(vntoascii('A') != vntoascii('b'))
    assert(ord(vntoascii('A')) == 101)
    assert(ord(vntoascii('À')) == 102)
    assert(ord(vntoascii('Á')) == 103)
    assert(ord(vntoascii('Ả')) == 104)
    assert(ord(vntoascii('Ã')) == 105)
    assert(ord(vntoascii('Ạ')) == 106)
    assert(ord(vntoascii('Ă')) == 107)
    assert(ord(vntoascii('Ằ')) == 108)
    print("All passed. Done!!!")
    
def test():
    """Tests using assert()."""
    print(f"{len(vn_lowercase)}-{len(vn_uppercase)}")
#
    test_vn_ascii()
#
    name_str = "Nga Đức Duy Ánh Anh Hằng"
    names = name_str.split()
    sorted_names = sorted(names, key = vntoascii)
    print(names)
    print(sorted_names)
    names = ["Nguyễn Duy Thể", "Trần Thị Phương Anh", "Nguyễn Việt Anh"]
    sorted_names = sorted(names, key = vntoascii)
    print(names)
    print(sorted_names)
# Tên ở trên chưa được sắp xếp đúng do hàm vntoascii được áp dụng lên toàn bộ tên chứ không phải lên từng phần họ, tên, tên đệm và ưu tiên so sánh tên rồi tới họ rồi cuối cùng mới tới tên đệm.
#
    test_VnFullName()
#
    
if __name__ == "__main__":
    """Test commands go here."""
    test()
