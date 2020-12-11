"""
Vietnamese related!!!
"""
vn_lowercase=" aàáảãạăằắẳẵặâầấẩẫậbcdđeèéẻẽẹêềếểễệfghiìíỉĩịjklmnoòóỏõọôồốổỗộơờớởỡợpqrstuùúủũụưừứửữựvwxyỳýỷỹỵz"
vn_uppercase=" AÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬBCDĐEÈÉẺẼẸÊỀẾỂỄỆFGHIÌÍỈĨỊJKLMNOÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢPQRSTUÙÚỦŨỤƯỪỨỬỮỰVWXYỲÝỶỸỴZ"
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

def test():
    """Tests using assert()."""
    print(f"{len(vn_lowercase)}-{len(vn_uppercase)}")
    name_str = "Nga Đức Duy Ánh Anh Hằng"
    names = name_str.split()
    sorted_names = sorted(names, key = vntoascii)
    print(names)
    print(sorted_names)
    names = ["Nguyễn Duy Thể", "Trần Thị Phương Anh", "Nguyễn Việt Anh"]
    sorted_names = sorted(names, key = vntoascii)
    print(names)
    print(sorted_names)
    print("Testing...")
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
    
if __name__ == "__main__":
    """Test commands go here."""
    test()
