class Node:
    def __init__(self, key):
        self.key = key # Value of the node
        self.left = None # Reference to the left child node
        self.right = None # Reference to the right child node

class BST:
    def __init__(self):
        self.root = None # Reference to the root node of the Binary Search Tree (BST)
    
    def insert(self, key):
        if self.root is None: # If the tree is empty
            self.root = Node(key) # Create a new node and set it as the root
        else:
            self._insert_recursive(self.root, key) # Call the recursive insert function with the root

    def _insert_recursive(self, current_node, key):
        if key < current_node.key: # If the key is less than the current node's key
            if current_node.left is None: # If the left child is empty
                current_node.left = Node(key) # Create a new node and set it as the left child
            else:
                self._insert_recursive(current_node.left, key) # Recursively insert in the left subtree
        elif key > current_node.key: 
            if current_node.right is None: # If the right child is empty
                current_node.right = Node(key) # Create a new node and set it as the right child
            else:
                self._insert_recursive(current_node.right, key) # Recursively insert in the right subtree
        # if key == current_node.key, it's a duplicate and typically not inserted in a strict BST.

    def search(self, key):
        return self._search_recursive(self.root, key) # Call the recursive search function with the root

    def search_recursive(self, current_node, key):
        if current_node is None or current_node.key == key: # If the node is None of the key is found
            return current_node # Return the node (found) or None (not found)
        if key < current_node.key: # If the key is less than the current node's key
            return self._search_recursive(current_node.left, key) # Recursively search in the left subtree
        else:
            return self._search_recursive(current_node.right, key) # Recursively search in the right subtree

    def inorder_traversal(self):
        result = [] # List to store the inorder traversal result
        self._inorder_recursive(self.root, result) # Call the recursive inorder function with the root
        return result # Return the inorder traversal result

    def _inorder_recursive(self, current_node, result):
        if current_node:
            self._inorder_recursive(current_node.left, result) # Traverse the left subtree
            result.append(current_node.key) # Visit the current node
            self._inorder_recursive(current_node.right, result) # Traverse the right subtree

# Example usage:
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("In-order traversal:", bst.inorder_traversal()) # Expected: [20, 30, 40, 50, 60, 70, 80]

    node = bst.search(40)
    if node:
        print(f"Found node with key: {node.key}") # Expected: Found node with key: 40
    else:
        print("Node not found.")

    node = bst.search(90)
    if node:
        print(f"Found node with key: {node.key}")
    else:
        print("Node not found.") # Expected: Node not found.
