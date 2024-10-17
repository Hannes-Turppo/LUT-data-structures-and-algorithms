class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self, mirrored=False):
        self.root = None
        self.mirrored = mirrored

    # insert a key in the tree
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_recursive(self.root, key)

    def insert_recursive(self, current, key): # Recursive component
        if self.mirrored:   # If the tree is mirrored.
            if key > current.key:
                if current.left is not None:
                    self.insert_recursive(current.left, key)
                else:
                    current.left = Node(key)
            elif key < current.key:
                if current.right is not None:
                    self.insert_recursive(current.right, key)
                else:
                    current.right = Node(key)

        else:   # For normal tree.
            if key < current.key:
                if current.left is not None:
                    self.insert_recursive(current.left, key)
                else:
                    current.left = Node(key)
                    # print(current.key, current.left.key, "left")
            elif key > current.key:
                if current.right is not None:
                    self.insert_recursive(current.right, key)
                else:
                    current.right = Node(key)
                    # print(current.key, current.right.key, "right")


    # search for a key in the tree
    def search(self, key):
        if self.root is None:
            return False
        return self.search_recursive(self.root, key)

    def search_recursive(self, current, key):
        if current is None:
            return False
        if key == current.key:
            return True
        elif key < current.key:
            return self.search_recursive(current.left, key) if not self.mirrored else self.search_recursive(current.right, key)
        else:
            return self.search_recursive(current.right, key) if not self.mirrored else self.search_recursive(current.left, key)

    # remove a key from the tree
    def remove(self, key):
        if self.root is None:
            return
        self.root = self.remove_recursive(self.root, key)

    def remove_recursive(self, current, key):
        if current is None:
            return current
        if self.mirrored:  # if tree is mirrored
            if key > current.key:
                current.left = self.remove_recursive(current.left, key)
            elif key < current.key:
                current.right = self.remove_recursive(current.right, key)
            else:
                if current.left is None and current.right is None:
                    return None
                elif current.left is None:
                    return current.right
                elif current.right is None:
                    return current.left
                temp = self.find_max(current.right)  # find the maximum in the right subtree
                current.key = temp.key
                current.right = self.remove_recursive(current.right, temp.key)

        else:  # for normal tree
            if key < current.key:
                current.left = self.remove_recursive(current.left, key)
            elif key > current.key:
                current.right = self.remove_recursive(current.right, key)
            elif key == current.key:
                if current.left is None and current.right is None:
                    return None
                elif current.left is None:
                    return current.right
                elif current.right is None:
                    return current.left
                temp = self.find_min(current.right)  # find the minimum in the right subtree
                current.key = temp.key
                current.right = self.remove_recursive(current.right, temp.key)
        return current


    # find minimum value in subtree
    def find_min(self, current):
        if self.mirrored:  # if tree is mirrored
            while current.right is not None:
                current = current.right
        else:
            while current.left is not None:
                current = current.left
        return current

    # find maximum value in subtree
    def find_max(self, current):
        if self.mirrored:
            while current.left is not None:
                current = current.left
        else:
            while current.right is not None:
                current = current.right
        return current


    # print tree in preorder
    def preorder(self):
        if self.root is not None:
            self.preorder_recursive(self.root)
        print() #newrow

    def preorder_recursive(self, current): # Recursive component
        if current is None:
            return
        print(current.key, end=' ')
        self.preorder_recursive(current.left)
        self.preorder_recursive(current.right)
        return


    # breadth first search
    def breadthfirst(self):     # ToDo
        if self.root is None:
            return
        self.breadthfirst_recursive(self.root)
        print() #newrow
        return
    
    # Imitated from https://www.geeksforgeeks.org/level-order-tree-traversal/
    def breadthfirst_recursive(self, current): # Recursive component
        if current is None:
            return
        
        # initialize queue
        queue = []
        queue.append(current)

        while len(queue) > 0:
            print(queue[0].key, end=' ')
            node = queue.pop(0) # Traverse the node

            if node.left is not None: # Add left child to queue
                queue.append(node.left)

            if node.right is not None: # Add right child to queue
                queue.append(node.right)

        return


    # Inorder traversal
    def inorder(self):
        if self.root is None:
            return None
        # print in inorder
        self.inorder_recursive(self.root)
        print() #newrow
        return

    def inorder_recursive(self, current):
        if current is None:
            return
        # print in the middle so the print order is left->root->right
        self.inorder_recursive(current.left)
        print(current.key, end=' ')
        self.inorder_recursive(current.right)
        return


    # Postorder traversal
    def postorder(self):
        if self.root is None: # check if tree is empty
            return None
        # print in postorder
        self.postorder_recursive(self.root)
        print() #newrow
        return

    def postorder_recursive(self, current): # postorder recursive function
        if current is None:
            return
        # print after traversal so the print starts from the bottom of the tree
        self.postorder_recursive(current.left)
        self.postorder_recursive(current.right)
        print(current.key, end=' ')
        return


    # mirror the tree
    def mirror(self):
        self.root = self.mirror_recursive(self.root)
        self.mirrored = not self.mirrored

    def mirror_recursive(self, current):
        if current is None:
            return current
        current.left, current.right = current.right, current.left # swap left and right
        self.mirror_recursive(current.left)
        self.mirror_recursive(current.right)
        return current


if __name__ == "__main__":
    tree = BST()
    tree.mirror()

    for num in (9, 8, 13, 4, 11, 14, 3, 6, 10, 12, 26, 2, 5, 7, 20, 29):
        tree.insert(num)

    tree.inorder()

    tree.remove(2)
    tree.remove(13)

    tree.preorder()

    tree.mirror()

    for num in (5, 7, 11, 10, 12, 20, 29):
        tree.insert(num)

    tree.preorder()