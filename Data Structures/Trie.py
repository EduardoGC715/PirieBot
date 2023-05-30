import re
from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, t_pattern, t_value):
        """Insert a pattern into the trie"""
        node = self.root

        # Loop through each character in the pattern
        # Check if there is no child containing the character, create a new child for the current node
        for char in t_pattern:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a pattern and store the associated value
        node.is_end = True
        node.value = t_value

    def dfs(self, t_node, t_message, t_prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - message: the input message to match against
            - prefix: the current prefix, for tracing a
                pattern while traversing the trie
        """
        if t_node.is_end:
            regex = "^" + t_prefix + t_node.char + "$"
            match = re.search(regex, t_message, re.IGNORECASE)
            if match:
                return t_node.value

        for child in t_node.children.values():
            result = self.dfs(child, t_message, t_prefix + t_node.char)
            if result:
                return result

        return None

    def find_matching_value(self, t_message):
        """Given an input message, retrieve the first matching value
        stored in the trie based on the patterns
        """
        node = self.root

        # Traverse the trie to find a matching value
        result = self.dfs(node, t_message, "")
        return result
