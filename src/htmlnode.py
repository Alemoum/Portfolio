# Creating a new class
class HTMLNode():
    
    def __init__(self, tag= None, value=None, children=None, props=None):
        
        self.tag = tag # String representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        
    # Child classes will override this method to render themselves as HTML
    def to_html(self):
        
        if self.children:
            child_html_list = [child.to_html() for child in self.children]
            children_html = "".join(child_html_list)
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
        elif self.value:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        else:
            return ""
        
    # Return a string that represents the HTML attributes of the node
    def props_to_html(self):
        
        result = "" 
        if self.props != None: # Veryfing if props exist
            for key in self.props: # Iterating over each key
                result += f' {key}="{self.props[key]}"' # Adding the key and value to a formated string 
            return result 
        else:
            return "" # If there's no props, just return an empty string
    
    # Give a way to print an HTMLNode object and see its tag, value, children, and props
    def __repr__(self):

        return f"HTMLNode({self.tag, self.value, self.children, self.props})"
    

    