#\\\IMPORTS///
import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        
        child_node = LeafNode("b", "Click me!", {'href':"https://google.com"})
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<p><b href="https://google.com">Click me!</b></p>'
        )
    
    def test_child_with_missing_tag(self):
        
        child_node = LeafNode(None, "this is a sentence")
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<p>this is a sentence</p>"
        )
        
    
    
if __name__ == "__main__":
    unittest.main()

