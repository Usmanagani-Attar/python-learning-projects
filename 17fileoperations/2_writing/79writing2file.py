txt_data = "I like chicken"
file_path =r"C:\Users\Dell\Documents\Desktop\5th sem\python\Python\17fileoperations\2_writing\second.txt"

with open(file_path,"w") as file:
    file.write(txt_data)
    print(f"Text file {file_path} was created")