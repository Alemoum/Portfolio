from enum import Enum # Importing enum for the inline types

# Enumerate types of inline
class TextType(Enum):
     TEXT = "text"
     BOLD = "bold"
     ITALIC = "italic"
     CODE = "code"
     LINK = "link"
     IMAGE = "image"
     
# Creating the class 
class TextNode():
     
     # Set up for constructor 
    def __init__(self, text, text_type, url=None): 
         
        self.text = text # Text itself
        self.text_type = text_type # Type of the text (bold, italic, etc)
        self.url = url # Url if its have, otherwise its none
    
    # Method to check if a text node is equal to other one
    def __eq__(self, other):
         
         if self.text == other.text and self.text_type == other.text_type and self.url == other.url: # Comparing all properties from the classes 
              return True # If its equal returne True
         else:
              return False # Different return False
       
     # Method to return a string showing the properties from the Node
    def __repr__(self):
         
          return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


