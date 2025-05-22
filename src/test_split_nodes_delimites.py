#\\\IMPORTS///
import unittest
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_one_node(self):
        random_node = TextNode("this is a**bold**sentence", TextType.TEXT)
        result = split_nodes_delimiter([random_node], "**", TextType.BOLD)
        self.assertEqual([node.text for node in result], ["this is a", "bold", "sentence"])
        self.assertEqual([node.text_type for node in result], [TextType.TEXT, TextType.BOLD, TextType.TEXT])
    
    def test_no_delimiters_in_text(self):  # Note: fixed method name to include "test_"
        node = TextNode("This text has no delimiters", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This text has no delimiters")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        
    def test_multiple_delimited_sections(self):
        node = TextNode("This has **two** separate **bold** sections", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 5)
        self.assertEqual([node.text for node in result], 
                        ["This has ", "two", " separate ", "bold", " sections"])
        self.assertEqual([node.text_type for node in result],
                        [TextType.TEXT, TextType.BOLD, TextType.TEXT, TextType.BOLD, TextType.TEXT])

    def test_already_delimited_node(self):
        # Test that non-TEXT nodes are preserved as is
        bold_node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_delimiter([bold_node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "already bold")
        self.assertEqual(result[0].text_type, TextType.BOLD)

    def test_missing_closing_delimiter(self):
        node = TextNode("This text has **unclosed delimiter", TextType.TEXT)
        # Test that your function raises
    
    def test_split_nodes_image_no_images(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is text with no images")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    
    def test_split_nodes_image_one_image(self):
        node = TextNode(
            "This is text with an ![image](https://example.com/image.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "This is text with an ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "image")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "https://example.com/image.png")
    
                         
if __name__ == "__main__":
    unittest.main() 