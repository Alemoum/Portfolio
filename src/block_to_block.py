from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block):
    
    heading_list = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    
    for heading in heading_list:
        if block.startswith(heading):
            return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split('\n')
    
    quote_block = all(line.startswith("> ") for line in lines)
    unordered_list_block = all(line.startswith("- ") for line in lines)
    ordered_list_block = all(line.startswith(f"{index}. ") for index, line in enumerate(lines, start=1))
    
    if quote_block == True:
        return BlockType.QUOTE
    
    elif unordered_list_block == True:
        return BlockType.UNORDERED_LIST
    
    elif ordered_list_block == True:
        return BlockType.ORDERED_LIST
    
    else:
        return BlockType.PARAGRAPH
    
            