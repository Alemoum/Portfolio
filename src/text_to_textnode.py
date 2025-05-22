#\\\IMPORTS///
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnode(text):
    
    delimiters_types = [("_", TextType.ITALIC), ("**", TextType.BOLD), ("`", TextType.CODE)]
    node = (TextNode(text, TextType.TEXT))
    nodes = split_nodes_image(split_nodes_link([node]))
    
    for delimiter, type in delimiters_types:
        nodes = split_nodes_delimiter(nodes, delimiter, type)

    return nodes
    

