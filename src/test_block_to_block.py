#\\\IMPORTS///
import unittest
from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlock(unittest.TestCase):
    
    def test_code_block(self):
        sentence = "```\n This is a code block \n```"
        self.assertEqual(block_to_block_type(sentence), BlockType.CODE)

    def test_quote_block(self):
        sentence = "> This is a quote\n> Quote in another line\n> Final line"
        self.assertEqual(block_to_block_type(sentence), BlockType.QUOTE)
        
    def test_unordered_list(self):
        sentence = "- Unordered\n- List\n- Python"
        self.assertEqual(block_to_block_type(sentence), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        sentence= "1. Ordered\n2. List\n3. Python"
        self.assertEqual(block_to_block_type(sentence), BlockType.ORDERED_LIST)
        
    def test_heading_block(self):
        sentence = "#### Some text here"
        self.assertEqual(block_to_block_type(sentence), BlockType.HEADING)
        
    def test_paragraph_block(self):
        sentence = "> Just some paraprag\nPython block"
        sentence2 = "1. Ordered\n2. List\n4. Just kidding"
        sentence3 = "- Unordered\n- List\n Just kidding"
        sentence4 = "```Fake code block"
        sentence5 = "####### I think thats too many hashs"
        sentence6 = "Just plain text my boy"
        
        self.assertEqual(block_to_block_type(sentence), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(sentence2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(sentence3), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(sentence4), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(sentence5), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(sentence6), BlockType.PARAGRAPH)
        
    
        
if __name__ == "__main__":
    unittest.main()