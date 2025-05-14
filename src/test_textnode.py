import unittest

from textnode import TextNode, TextType

# Class of tests
class TestTextNode(unittest.TestCase):
    
    # Method to test if a node is equal to other
    def test_eq(self):
        
        node = TextNode("This is a text node", TextType.BOLD) # Creating a random node
        node2 = TextNode("This is a text node", TextType.BOLD)  # Creating a random node
        
        self.assertEqual(node, node2) # Unittest function to see if its equal

    # Method to test if a node text type property isn't equal to other
    def test_type_no_eq(self):
        
        node = TextNode("This is a text node", TextType.BOLD) # Creating a random node
        node2 = TextNode("This is a text node", TextType.ITALIC) # Creating a random node
        
        self.assertNotEqual(node, node2) # Unittest function to see if its equal
    
    # Method to test if text isn't equal to other
    def test_text_no_eq(self):
        
        node = TextNode("This is a text node", TextType.BOLD) # Creating a random node
        node2 = TextNode("This is another text node", TextType.BOLD) # Creating a random node
        
        self.assertNotEqual(node, node2) # Unittest function to see if its not equal
    
    # Method to test if url is equal to other
    def test_url_eq(self):
        
        node = TextNode("This is a text node", TextType.BOLD, None) # Creating a random node
        node2 = TextNode("This is a text node", TextType.BOLD, None) # Creating a random node
        
        self.assertEqual(node, node2) # Unittest function to see if its equal
    
    # method to test if url's are different
    def test_different_url(self):
        
        node = TextNode("This is a text node", TextType.BOLD, None) # Creating a random node
        node2 = TextNode("This is a text node", TextType.BOLD, "www.boot.dev") # Creating a random node
        
        self.assertNotEqual(node, node2) # Unittest function to see if its not equal
        
if __name__ == "__main__":
    unittest.main()