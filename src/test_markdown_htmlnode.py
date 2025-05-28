#\\\IMPORTS///
import unittest
from markdown_htmlnode import markdown_to_htmlnode
from htmlnode import HTMLNode
class TestMarkdownHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_headings(self):
        md = """
         ### **There some headings**
        """
        
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(html,
                         "<div><h3><b>There some headings</b></h3></div>"
                         )
        
    def test_ordered_list(self):
        md = """
         1.  **This is**
         2.  A ordered
         3.  List
        """
        
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(html,
                         "<div><ol><li><b>This is</b></li><li>A ordered</li><li>List</li></ol></div>"
                         )
    
    def test_unordered_list(self):
        md = """
        -. _This is_
         -. Unordered
         -.   **List**
        """

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(html,
                         "<div><ul><li><i>This is</i></li><li>Unordered</li><li><b>List</b></li></ul></div>"
                         )
    
    def test_quote_block(self):
        md = """
        > This is a quote with **bold**
        > and _italic_ text
        """
        
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(html,
                         "<div><blockquote>This is a quote with <b>bold</b> and <i>italic</i> text</blockquote></div>"
                         )
        
    
if __name__ == "__main__":
    unittest.main()