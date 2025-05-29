import os

path = "lalala.md"

list_splited_text = list(os.path.splitext(path))
list_splited_text[1] = ".html"
new_path = list_splited_text[0] + list_splited_text[1]

print(new_path)