import os
file_path=r"C:\Users\Dell\Documents\Desktop\5th sem\python\Python\17fileoperations\detection\file.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} is exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is directory")

else:
    print("The location doesn't exist ")