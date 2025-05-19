#\\\IMPORTS///
import unittest # Importing unit test library
from htmlnode import HTMLNode # Importing class from htmlnode.py


class TestHTMLNode(unittest.TestCase):
    
    def test_props_is_none(self):
        
        random_html_node = HTMLNode ( props = None ) # Setting a random html node
        self.assertIsNone ( random_html_node.props) 
        
    def test_props_not_none(self):
        
        random_html_node = HTMLNode ( props = "" ) # Setting a random html node
        self.assertIsNotNone ( random_html_node.props) 
        
    def test_props_to_html_single_prop(self):
        
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple_props(self):
        
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertTrue(' href="https://example.com"' in node.props_to_html())
        self.assertTrue(' target="_blank"' in node.props_to_html())

    def test_props_to_html_none_props(self):
        
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")
    
if __name__ == "__main__":
    unittest.main()