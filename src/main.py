#\\\IMPORTS///
import os
import shutil

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
                
                print(path)
                shutil.copy(path, dest_dir)
                
            else:
                
                destination = os.path.join(dest_dir, dir)
                
                if not os.path.exists(destination):
                    os.mkdir(destination)
                    
                paste_files(path, destination)
                
    paste_files("static", "public")
        
        
def main():
    
    copy_directory()
    
main()
