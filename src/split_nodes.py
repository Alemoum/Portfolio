#\\\IMPORTS///
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


node = TextNode(
    "This is text with a link [**to boot dev**](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    list_of_nodes = [] 
    
    for old_node in old_nodes: # Iterating over the list of old_nodes
        
        if old_node.text_type != TextType.TEXT: # Checking if the node isn't normal text
            
            list_of_nodes.append(old_node) # If isn't just return the node 
            
        else:
            splited_text = old_node.text.split(delimiter) # If it is, split the text by delimiter
            
            if len(splited_text) % 2 == 0: # If the len is an odd number the delimiter was not closed properly on text
                    raise Exception("that's invalid Markdown syntax.")
                
            for index, value in enumerate(splited_text): # Enumerate the splited text to acces the index 
                
                if index % 2 == 0 and value != "": # If the index is an even number its a regular text
                    list_of_nodes.append(TextNode(value, TextType.TEXT))
                elif index % 2 != 0 and value != "": 
                    list_of_nodes.append(TextNode(value, text_type))    
    
    return list_of_nodes

def split_nodes_link(old_nodes):
    result = []
    
    for old_node in old_nodes:
        # Only process text nodes
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
        links = extract_markdown_links(old_node.text)
        
        if not links:
            result.append(old_node)
            continue
        
        # Process the first link
        alt_text, link_url = links[0] 
        delimiter = f"[{alt_text}]({link_url})"
        sections = old_node.text.split(delimiter, 1)
        
        
        # Add text before the link if it exists
        if sections[0]:
            result.append(TextNode(sections[0], TextType.TEXT))
            
        # Add the link node
        result.append(TextNode(alt_text, TextType.LINK, link_url))
        
        # If there's text after the link, process it for more links
        if len(sections) > 1 and sections[1]:
            # Create a new node for the remaining text
            remaining_node = TextNode(sections[1], TextType.TEXT)
            # Process it recursively
            result.extend(split_nodes_link([remaining_node]))
    
    return result
            
                
            
        
        
def split_nodes_image(old_nodes):
    result = []
    
    for old_node in old_nodes:
        # Only process text nodes
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
        images = extract_markdown_images(old_node.text)
        
        if not images:
            result.append(old_node)
            continue
        
        # Process the first image
        alt_text, image_url = images[0]
        delimiter = f"![{alt_text}]({image_url})"
        sections = old_node.text.split(delimiter, 1)
        
        # Add text before the image if it exists
        if sections[0]:
            result.append(TextNode(sections[0], TextType.TEXT))
            
        # Add the image node
        result.append(TextNode(alt_text, TextType.IMAGE, image_url))
        
        # If there's text after the image, process it for more images
        if len(sections) > 1 and sections[1]:
            # Create a new node for the remaining text
            remaining_node = TextNode(sections[1], TextType.TEXT)
            # Process it recursively
            result.extend(split_nodes_image([remaining_node]))
    
    return result
    

print(split_nodes_link([node]))