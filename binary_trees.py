# binary Tree
# top node is called the root
# in a binary tree each node has at most two children left right
# parent and child relationship
#node at the very bottom are called leaves 
# depth of the tree including root and leaves 
# height is the opposite

# different types of binary trees 
# complete binary tree all levels except the last level (so not all the leaves) and the leaves are on the left

# Full tree: every space is complete

# many ways of traversing the tree


class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None



class BinaryTree:
  def __init__(self, root):
    self.root = Node(root)

  def print_tree(self, traversal_type):
    if traversal_type == 'preorder':
      return self.preorder_print(tree.root, "")

    elif traversal_type == 'inorder':
      return self.inorder_print(tree.root, "")
    
    elif traversal_type == 'postorder':
      return self.postorder_print(tree.root, "")
    
    else:
      print(f'travesal type {traversal_type} does not exist')
      return False


  # dept first search - in order, pre order and post order
  def preorder_print(self, start, traversal):
    """Root => Left => Right"""

    if start:
      traversal += (str(start.value) + "-")
      traversal = self.preorder_print(start.left, traversal)
      traversal = self.preorder_print(start.right, traversal)
    return traversal

  
  def inorder_print(self,start, traversal):
    """ left root right"""
    # go left as far as you can
    if start:
      traversal = self.inorder_print(start.left, traversal)
      traversal += (str(start.value) + "-")
      traversal = self.inorder_print(start.right, traversal)
    return traversal

  def postorder_print(self,start, traversal):
    """ left right root"""
    # go left as far as you can
    if start:
      traversal = self.inorder_print(start.left, traversal)
      traversal = self.inorder_print(start.right, traversal)
      traversal += (str(start.value) + "-")
    return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


#           1 
#         /   \
#        2     3
#       / \   / \
#      4   5 6   7

print(tree.print_tree('postorder'))