class TrieNode:
    def __init__(self, t_char):
        self.children = {}
        self.char = t_char
        self.is_end = False
        self.counter = 0
