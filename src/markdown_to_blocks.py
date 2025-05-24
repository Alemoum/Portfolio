#\\\IMPORTS//

def markdown_to_blocks(markdown):
    splited_text = markdown.split("\n\n")
    new_list = []
    
    for blocks in splited_text:
        striped_blocks = blocks.strip()
        
        if "\n" in striped_blocks:
            splited_lines = striped_blocks.split("\n")
            lines_list = []
            for line in splited_lines:
                striped_line = line.strip()
                lines_list.append(striped_line)
            striped_blocks = "\n".join(lines_list)

        if striped_blocks != "":
            new_list.append(striped_blocks)
    return new_list

