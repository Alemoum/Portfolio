#\\\IMPORTS///
from textnode import TextNode, TextType

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
    
