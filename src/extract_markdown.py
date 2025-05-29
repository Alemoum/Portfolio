#\\\IMPORTS///
import re 

def extract_markdown_images(text):
    
    matches_images = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    if matches_images == []:
        return []
    return matches_images

def extract_markdown_links(text):
    
    matches_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if matches_links == []:
        return []
    return matches_links




