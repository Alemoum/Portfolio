#\\\IMPORTS///
from markdown_to_blocks import markdown_to_blocks
from block_to_block import block_to_block_type,BlockType
from htmlnode import HTMLNode
from text_to_textnode import text_to_textnode
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType
import re

def text_to_children(text):
        html_nodes = []
        list_of_text_nodes = text_to_textnode(text)
        for text_node in list_of_text_nodes:
            html_nodes.append(text_node_to_html_node(text_node))
        return html_nodes
    
def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    list_of_nodes = []
    
    for block in blocks:
        
        type_of_block = block_to_block_type(block)
        
        #\\\ HEADINGS ///
        if type_of_block == BlockType.HEADING:
            find_head = "".join(re.findall("^#+", block))
            list_of_nodes.append(HTMLNode(f"h{len(find_head)}", None, text_to_children(block[len(find_head):].strip())))
    
        #\\\ CODE ///    
        elif type_of_block == BlockType.CODE:
            lines = block.split("\n")
            list_of_lines = []
            for line in lines:
                if line.startswith("```"):
                    pass
                else:
                    list_of_lines.append(line)
            text_code = text_node_to_html_node(TextNode("\n".join(list_of_lines) + "\n", TextType.CODE))
            list_of_nodes.append(HTMLNode("pre", None, [text_code]))
        
        #\\\ QUOTE ///    
        elif type_of_block == BlockType.QUOTE:
            
            lines = block.split("\n")
            list_of_lines = []
            
            for line in lines:
                if line.startswith("> "):
                    list_of_lines.append(line[2:])
                elif line.startswith(">"):
                    list_of_lines.append(line[1:])
                else:
                    list_of_lines.append(line)
                    
            list_of_nodes.append(HTMLNode("blockquote", None, text_to_children(" ".join(list_of_lines))))
        
        #\\\ UNORDERED LIST ///  
        elif type_of_block == BlockType.UNORDERED_LIST:
            
            lines = block.split("\n")
            list_of_lines = []
            
            for line in lines:
                
                match = re.match(r"^\s*[-*+][.\s]+", line)
                
                if match:
                    content = line[match.end():]
                    list_of_lines.append(HTMLNode("li", None, text_to_children(content.strip())))
            list_of_nodes.append(HTMLNode("ul", None, list_of_lines))

        
        #\\\ ORDERED LIST ///  
        elif type_of_block == BlockType.ORDERED_LIST:
            
            lines = block.split("\n")
            list_of_lines = []
            
            for line in lines:
                match = re.match("^\\d+\\. ", line)
                
                if match: 
                    content = line[match.end():]
                    list_of_lines.append(HTMLNode("li", None, text_to_children(content.strip())))
                    
            list_of_nodes.append(HTMLNode("ol", None, list_of_lines))
        
        #\\\ PARAGRAPH ///  
        elif type_of_block == BlockType.PARAGRAPH:
            paragraph_text = " ".join(block.splitlines()).strip()
            list_of_nodes.append(HTMLNode("p", None, text_to_children(paragraph_text)))
    
    main_node = HTMLNode("div", None, list_of_nodes)
    return main_node