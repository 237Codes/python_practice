class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

lst = []
def process_node(node, lst):
    current = node
    if current == None:
      return None
    if current.left:
        return process_node(current.left, lst)
    lst.append(current.val) 
    if current.right:
        return process_node(current.right, lst)
          
def is_symmetric(root):
    process_node(root, lst)
    print(lst)
    if len(lst) % 2 == 0:
        return False
    else:
        i = len(lst) // 2 - 1
        j = len(lst) // 2 + 1
        while (j < len(lst)):
            if lst[i] == lst[j]:
                i = i - 1
                j = j + 1
            else:
                return False
        return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(7)
root.right.left =TreeNode(4)
root.left.right = TreeNode(4)
root.right.right =  TreeNode(5)
print(is_symmetric(root))