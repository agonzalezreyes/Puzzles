class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie(object):
    def __init__(self):
        self.root = self.getNode()
    
    # Empty Trie Node
    def getNode(self):
        return TrieNode()
    
    # converts key current character into index
    def _charToIndex(self, char):
        return ord(char)-ord('a')
    
    """
    if not present, inserts key into trie
    if the key is prefix of trie node, marks leaf node
    """
    def insert(self, key):
        parent = self.root
        length = len(key)
        for level in range(length):
            # char = key[level] to index
            index = self._charToIndex(key[level])
            # if curr char is not present
            if not parent.children[index]:
                parent.children[index] = self.getNode()
            parent = parent.children[index]
        # mark last node as leaf
        parent.isEnd = True
    
    """
    search key in the trie
    returns true if present, else returns false
    """
    def search(self, key):
        parent = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not parent.children[index]:
                return False
            parent = parent.children[index]
        return parent != None and parent.isEnd


