#\\\IMPORTS///
import os
import shutil
from markdown_to_html_node import markdown_to_htmlnode, extract_title
import pathlib

def copy_directory():
    
    if not os.path.exists("public"):
        
        os.mkdir("public")
        
    else:
        
        shutil.rmtree("public")
        os.mkdir("public")
        
    def paste_files(source_dir, dest_dir):
        
        for dir in os.listdir(source_dir):
            
            path = os.path.join(source_dir,dir)
            
            if os.path.isfile(path):
                
                shutil.copy(path, dest_dir)
                
            else:
                
                destination = os.path.join(dest_dir, dir)
                
                if not os.path.exists(destination):
                    os.mkdir(destination)
                    
                paste_files(path, destination)
                
    paste_files("static", "public")
        

def generate_page(from_path, template_path, dest_path):
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as fp:
        markdown_file = fp.read()
   
    
    with open(template_path) as tp:
        template_file = tp.read()
    
    
    html_node = markdown_to_htmlnode(markdown_file).to_html()
    title = extract_title(markdown_file)
    title_replacement = template_file.replace("{{ Title }}", title)
    content_replacement = title_replacement.replace("{{ Content }}", html_node)
    
    direc = os.path.dirname(dest_path)
    if not os.path.exists(direc):
        
        os.makedirs(direc)
        
    with open(dest_path, "w") as dp:
        dp.write(content_replacement)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    list_of_dir = os.listdir(dir_path_content)
    
    for dir in list_of_dir:
        
        path = os.path.join(dir_path_content, dir)
        
        
                
        if os.path.isfile(path):
            
            path_object = pathlib.Path(os.path.join(dest_dir_path, dir))
            new_path = path_object.with_suffix(".html")
            
            
            generate_page(path, template_path, new_path)
            
        else:
            
            destination = (os.path.join(dest_dir_path, dir))
                
            os.makedirs(destination, exist_ok=True)

            generate_pages_recursive(path, template_path, os.path.join(dest_dir_path, dir))
        
        
    
def main():
    
    copy_directory()
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")
    
main()
