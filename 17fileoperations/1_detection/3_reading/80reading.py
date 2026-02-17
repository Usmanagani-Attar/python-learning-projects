file_path=r"C:\Users\Dell\Documents\Desktop\5th sem\python\Python\17fileoperations\3_reading\third.txt"

try:
    with open (file_path) as file:
        content=file.read()
        print(content)

except FileExistsError:
    print("File not exist")

except PermissionError:
    print("You don't have permission to read")