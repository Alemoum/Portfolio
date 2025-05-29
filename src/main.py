#\\\IMPORTS///
import os
import shutil
from markdown_to_html_node import markdown_to_htmlnode, extract_title
import pathlib
import sys


        
def copy_directory():
    
    if not os.path.exists("docs"):
        
        os.mkdir("docs")
        
    else:
        
        shutil.rmtree("docs")
        os.mkdir("docs")
        
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
                
    paste_files("static", "docs")
        

def generate_page(from_path, template_path, dest_path, base_path):
    
    #print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as fp:
        markdown_file = fp.read()
   
    
    with open(template_path) as tp:
        template_file = tp.read()
    
    
    html_node = markdown_to_htmlnode(markdown_file).to_html()
    title = extract_title(markdown_file)
    title_replacement = template_file.replace("{{ Title }}", title)
    content_replacement = title_replacement.replace("{{ Content }}", html_node)
    replace_href = content_replacement.replace('href="/', f'href="{base_path}"')
    replacer_src = replace_href.replace('src="/', f'src="{base_path}"')
    
    direc = os.path.dirname(dest_path)
    if not os.path.exists(direc):
        
        os.makedirs(direc)
        
    with open(dest_path, "w") as dp:
        dp.write(replacer_src)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    
    list_of_dir = os.listdir(dir_path_content)
    
    for dir in list_of_dir:
        
        path = os.path.join(dir_path_content, dir)
        
        
                
        if os.path.isfile(path):
            
            path_object = pathlib.Path(os.path.join(dest_dir_path, dir))
            new_path = path_object.with_suffix(".html")
            
            
            generate_page(path, template_path, new_path, base_path)
            
        else:
            
            destination = (os.path.join(dest_dir_path, dir))
                
            os.makedirs(destination, exist_ok=True)

            generate_pages_recursive(path, template_path, os.path.join(dest_dir_path, dir), base_path)
        
        
    
def main():
    
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
        copy_directory()
        generate_page("content/index.md", "template.html", "docs/index.html", base_path)
        generate_pages_recursive("content", "template.html", "docs", base_path)
    else:
        base_path = "/"
        copy_directory()
        generate_page("content/index.md", "template.html", "docs/index.html", base_path)
        generate_pages_recursive("content", "template.html", "docs", base_path)
    
    
    
main()
