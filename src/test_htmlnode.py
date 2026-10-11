from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_node_children(self):
        # 1. Create the child nodes
        child_node_1 = HTMLNode("b", "bold text")
        child_node_2 = HTMLNode("i", "italic text")
        
        # 2. Put them in a list
        children_list = [child_node_1, child_node_2]
        
        # 3. Create a parent node and pass the children list
        # (Assuming your constructor order is: tag, value, children, props)
        parent_node = HTMLNode("p", None, children_list, None)
        
        # 4. Assert that the parent stored the exact list we gave it
        self.assertEqual(parent_node.children, children_list)
        
        # 5. (Optional but good practice) Assert specific details about the children
        self.assertEqual(len(parent_node.children), 2)
        self.assertEqual(parent_node.children[0].tag, "b")
        self.assertEqual(parent_node.children[1].value, "italic text")
        def test_leaf_to_html_p(self):
            node = LeafNode("p", "Hello, world!")
            self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

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
        def test_text(self):
            node = TextNode("This is a text node", TextType.TEXT)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()