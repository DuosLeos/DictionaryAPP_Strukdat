# class Node:
#     # if color = 0  -> red
#     # if color = 1  -> black
#     def __init__(self, key):  # Constructor
#         self.key = key  # Node membutuhkan key untuk diinisialisasi
#         self.parent = None
#         self.right = None
#         self.left = None
#         self.color = 0


# class RedBlackTree:
#     def __init__(self):  # Constructor
#         self.nol = Node(None)
#         self.nol.color = 1  # root dan nilai nol berwarna hitam
#         self.root = self.nol
#         self.number_of_nodes = 0

#     def search(self, key):
#         node = self.root

#         while node != self.nol:  # selama kita tidak mencapai ujung tree
#             if node.key == key:
#                 return True
#             elif key < node.key:
#                 node = node.left
#             else:
#                 node = node.right
#         return False

#     def insert(self, key):
#         newNode = Node(str(key).lower())
#         newNode.left = self.nol
#         newNode.right = self.nol
#         node = self.root
#         parent = None  # TBD

#         while node != self.nol:  # temukan parent yang tepat
#             parent = node
#             if newNode.key < node.key:
#                 node = node.left
#             else:
#                 node = node.right
#         newNode.parent = parent

#         if parent is None:  # Node yang diinsert adalah node pertama
#             newNode.color = 1
#             self.root = newNode
#             self.number_of_nodes += 1
#             return
#         elif newNode.key < parent.key:
#             parent.left = newNode
#         else:
#             parent.right = newNode

#         if newNode.parent.parent is None:  # Parent adalah root
#             self.number_of_nodes += 1
#             return

#         self.insertFix(newNode)  # Handle cases
#         self.number_of_nodes += 1

#     # method ini menangani kasus penginsertan red balck tree
#     def insertFix(self, newNode):
#         while newNode != self.root and newNode.parent.color == 0:  # looping samapai rooot atau induk berawara hitam
            
#             parentIsLeft = False  # Parent dianggap left child secara default

#             # tetapkan uncle ke simpul yang sesuai
#             if newNode.parent == newNode.parent.parent.left:
#                 uncle = newNode.parent.parent.right
#                 parentIsLeft = True
#             else:
#                 uncle = newNode.parent.parent.left

#             # Case 1: Uncle red -> warna kebalikan dari uncle, parent and grandparent
#             if uncle.color == 0:
#                 newNode.parent.color = 1
#                 uncle.color = 1
#                 newNode.parent.parent.color = 0
#                 newNode = newNode.parent.parent

#             # Case 2: Uncle black -> check triangular atau linear dan putar sesuai itu
#             else:
#                 # Case 2: Uncle  black -> check triangular or linear dan putar sesuai itu

#                 if parentIsLeft and newNode == newNode.parent.right:
#                     newNode = newNode.parent  # take care saat kita menjadikan simpul baru sebagai induk
#                     self.leftRotate(newNode)
#                 # Right-Left condition (triangular)
#                 elif not parentIsLeft and newNode == newNode.parent.left:
#                     newNode = newNode.parent
#                     self.rightRotate(newNode)
#                 # Left-left condition (linear)
#                 if parentIsLeft:
#                     newNode.parent.color = 1  # the new parent
#                     newNode.parent.parent.color = 0  # the new grandparent akan berawarna red
#                     self.rightRotate(newNode.parent.parent)
#                 # Right-right condition (linear)
#                 else:
#                     newNode.parent.color = 1
#                     newNode.parent.parent.color = 0
#                     self.leftRotate(newNode.parent.parent)

#         self.root.color = 1  # Set root menjadi black