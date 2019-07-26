class BinaryTree:
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self,value):
        if not self.value:
            self.value = value
        elif value < self.value:
            if not self.left:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

    def contains(self,value):
        if self.value == value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(value)
            else:
                return False
        