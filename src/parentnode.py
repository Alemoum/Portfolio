#\\\IMPORTS///
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = {}):
        
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        
        if self.tag is None:
            raise ValueError("Parent nodes must have tag value")
        
        elif self.children is None:
            raise ValueError("Parent nodees must have children value")
        
        else:
            
            final_string = ""
            for n in self.children:
                final_string += n.to_html()
            return f"<{self.tag}>{final_string}</{self.tag}>"
                

            