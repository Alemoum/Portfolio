#\\\IMPORTS///
import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_eq_no_props(self): # Testing a leafnode without props
        
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")
    
    def test_eq_props(self): # Testing a leafnode with props
        
        node = LeafNode("a", "This is a link", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">This is a link</a>')
        
    def test_no_tag(self): # Testing a leafnode without tag and props

        node = LeafNode(None, "this is a phrase")
        self.assertEqual(node.to_html(), "this is a phrase")
        
    def test_no_tag_props(self): # Testing a leafnode without 
        
        node = LeafNode(None, "this is a sentence", {'href: "https://www.google.com"'})
        self.assertEqual(node.to_html(), "this is a sentence")
        
if __name__ == "__main__":
    unittest.main()
