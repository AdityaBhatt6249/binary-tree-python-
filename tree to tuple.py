tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))

#convert to binary tree
class Treenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def track_tuple(data):

    if isinstance(data,tuple) and len(data)==3:
        node=Treenode(data[1])
        node.left=track_tuple(data[0])
        node.right=track_tuple(data[2])
    elif data is None:
        node=None
    else:
        node=Treenode(data)
    return node
tree1=track_tuple(tree_tuple)

#convert to tuple
def tree_to_tuple(node):
    if isinstance(node,Treenode):
        return(tree_to_tuple(node.left),node.key,tree_to_tuple(node.right))
    else:
        return node
tuple2=tree_to_tuple(tree1)
print(tuple2)

#to display the tree
def display_tree(node,space='\t',level=0):
    if node is None:
        print(space*level + "None")
        return
    elif node.left is None and node.right is None:
        print(space*level+str(node.key))
        return
    else:
        display_tree(node.right,space,level+1)
        print(space * level + str(node.key))
        display_tree(node.left, space, level + 1)

print(display_tree(tree1,'  '))

def tree_height(node):
    if node is None:
        return 0
    else:
        return 1+max(tree_height(node.left),tree_height(node.right))






