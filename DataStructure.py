class Node:
    # if color = 0  -> red
    # if color = 1  -> black
    def __init__(self, key):  # Constructor
        self.key = key  # Node membutuhkan key untuk diinisialisasi
        self.parent = None
        self.right = None
        self.left = None
        self.color = 0


class RedBlackTree:
    def __init__(self):  # Constructor
        self.nol = Node(None)
        self.nol.color = 1  # root dan nilai nol berwarna hitam
        self.root = self.nol
        self.number_of_nodes = 0

    def search(self, key):
        node = self.root

        while node != self.nol:  # selama kita tidak mencapai ujung tree
            if node.key == key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, key):
        newNode = Node(str(key).lower())
        newNode.left = self.nol
        newNode.right = self.nol
        node = self.root
        parent = None  # TBD

        while node != self.nol:  # temukan parent yang tepat
            parent = node
            if newNode.key < node.key:
                node = node.left
            else:
                node = node.right
        newNode.parent = parent

        if parent is None:  # Node yang diinsert adalah node pertama
            newNode.color = 1
            self.root = newNode
            self.number_of_nodes += 1
            return
        elif newNode.key < parent.key:
            parent.left = newNode
        else:
            parent.right = newNode

        if newNode.parent.parent is None:  # Parent adalah root
            self.number_of_nodes += 1
            return

        self.insertFix(newNode)  # Handle cases
        self.number_of_nodes += 1

    # method ini menangani kasus penginsertan red balck tree
    def insertFix(self, newNode):
        while newNode != self.root and newNode.parent.color == 0:  # looping samapai rooot atau induk berawara hitam
            
            parentIsLeft = False  # Parent dianggap left child secara default

            # tetapkan uncle ke simpul yang sesuai
            if newNode.parent == newNode.parent.parent.left:
                uncle = newNode.parent.parent.right
                parentIsLeft = True
            else:
                uncle = newNode.parent.parent.left

            # Case 1: Uncle red -> warna kebalikan dari uncle, parent and grandparent
            if uncle.color == 0:
                newNode.parent.color = 1
                uncle.color = 1
                newNode.parent.parent.color = 0
                newNode = newNode.parent.parent

            # Case 2: Uncle black -> check triangular atau linear dan putar sesuai itu
            else:
                # Case 2: Uncle  black -> check triangular or linear dan putar sesuai itu

                if parentIsLeft and newNode == newNode.parent.right:
                    newNode = newNode.parent  # take care saat kita menjadikan simpul baru sebagai induk
                    self.leftRotate(newNode)
                # Right-Left condition (triangular)
                elif not parentIsLeft and newNode == newNode.parent.left:
                    newNode = newNode.parent
                    self.rightRotate(newNode)
                # Left-left condition (linear)
                if parentIsLeft:
                    newNode.parent.color = 1  # the new parent
                    newNode.parent.parent.color = 0  # the new grandparent akan berawarna red
                    self.rightRotate(newNode.parent.parent)
                # Right-right condition (linear)
                else:
                    newNode.parent.color = 1
                    newNode.parent.parent.color = 0
                    self.leftRotate(newNode.parent.parent)

        self.root.color = 1  # Set root menjadi black

    def leftRotate(self, node):
        """
                node              y
                  \     =>      /  \
                    y         node  d
                  /  \           \
                c     d           c
                """
        y = node.right
        node.right = y.left  # connect node ke c
        if y.left != self.nol:  # connect c ke node
            y.left.parent = node

        y.parent = node.parent  # connect y ke node parent

        if node.parent is None:  # connect node parent ke y
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node  # connect y ke node
        node.parent = y  # connect node ke y

    def rightRotate(self, node):
        """
        node                    y
       /   \        =>        /   \
      y                     c    node
    /   \                        /
   c     d                      d
        """
        y = node.left
        node.left = y.right  # connect node ke d
        if y.right != self.nol:  # connect d ke node
            y.right.parent = node
        y.parent = node.parent  # connect y ke node parent

        if node.parent is None:  # connect b parent to a parent
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.right = node  # connect y ke node
        node.parent = y  # connect node ke y

    # method ini mererturn high of the tree
    def heightOfTree(self, node, sumval):
        if node is self.nol:
            return sumval
        return max(self.heightOfTree(node.left, sumval + 1), self.heightOfTree(node.right, sumval + 1))

    # method ini mereturns black-height of the tree
    def getBlackHeight(self):
        node = self.root
        bh = 0
        while node is not self.nol:
            node = node.left
            if node.color == 1:
                bh += 1
        return bh

    # function untuk print yang akan digunakan dalam debugging
    def __printCall(self, node, indent, last):
        if node != self.nol:
            print(indent, end=' ')  # default end character adalah new line
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 0 else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    # Function untuk mengeprint
    def print_tree(self):
        self.__printCall(self.root, "", True)


"""
tree = RedBlackTree()
tree.insert('a')
tree.insert('b')
tree.insert('e')
tree.insert('d')
tree.insert('c')
tree.insert('f')
tree.insert('g')
tree.insert('h')
tree.insert('i')
tree.insert('j')
tree.print_tree()
print(tree.heightOfTree(tree.root, 0))
print(tree.number_of_nodes)
print(tree.search('q'))
print(tree.getBlackHeight())
"""
