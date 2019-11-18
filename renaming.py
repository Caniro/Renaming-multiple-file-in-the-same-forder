import os

def fileRename():
    count = 0
    # forder address
    _address="C:\\Users\\caniro\\Desktop\\test"
    for file in os.listdir(_address):
        file_extension = os.path.splitext(file)[1]
        os.rename(_address + "\\"+file, _address + "\\"+"test("+str(count)+")"+file_extension)
        count += 1
    print("SUCCESS")

if __name__ == '__main__':
    fileRename()
