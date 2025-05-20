#\\\IMPORTS///
import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    
    def test_extract_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_link(self):
        matchces = extract_markdown_links(  
            "This is a text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matchces)
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another one ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matchces = extract_markdown_links(  
            "This is a text with a link [to boot dev](https://www.boot.dev) and another one [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to boot dev", "https://www.boot.dev")], matchces)
        
    def test_extract_with_nothing(self):
        
        matches_links = extract_markdown_links("Just a regular text")
        matches_images = extract_markdown_images("Just a regular text")
        
        self.assertListEqual([], matches_links)
        self.assertListEqual([], matches_images)
        
if __name__ == "__main__":
    unittest.main()