#\\\IMPORTS///
import unittest
from text_to_textnode import text_to_textnode
from textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
    
    def test_simple_text(self):
        
        sentence = text_to_textnode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(sentence,
                         [
                            TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
                            TextNode(" with an ", TextType.TEXT),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" word and a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" and an ", TextType.TEXT),
                            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.TEXT),
                            TextNode("link", TextType.LINK, "https://boot.dev"),
                         ])
        
    def test_plain_texts(self):
        
        sentence = text_to_textnode("This is just a plain text")
        self.assertEqual(sentence, [TextNode("This is just a plain text", TextType.TEXT)])

    def test_just_image(self):
        
        sentence = text_to_textnode("This is a ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(sentence,
                         [
                             TextNode("This is a ", TextType.TEXT),
                             TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
                         ])
    
    def test_multiple_links(self):
        
        sentence = text_to_textnode("Heres some text with a [link](https://boot.dev) then some text [link](https://boot.dev)")
        self.assertEqual(sentence, 
                         [
                             TextNode("Heres some text with a ", TextType.TEXT),
                             TextNode("link", TextType.LINK, "https://boot.dev"),
                             TextNode(" then some text ", TextType.TEXT),
                             TextNode("link", TextType.LINK, "https://boot.dev")
                         ])
    
    def test_adjacent_formatting(self):
        sentence = text_to_textnode("Theres a **bold text**_italic text_")
        self.assertEqual(sentence,
                         [
                             TextNode("Theres a ", TextType.TEXT),
                             TextNode("bold text", TextType.BOLD),
                             TextNode("italic text", TextType.ITALIC)
                         ])

if __name__ == "__main__":
    unittest.main() 