# -*- coding: utf-8 -*-
# Implementation of Binary Tree
# A node only saves the references to its children
#HOLAAAAAAAAAAAAAAAA

#transition model for the markov chain below sir:

def T(s1:State,a:Action, s2:State):
    #now, since it is an stochastic mdp, there is some noise when taking an action a from state s, potentially transitioning to state s2 with some certainty
    if a == "on": #for the action of turning the thermostat on...
        if s1.temperature == 16:
            if s2.temperature == 16:
                return 0.3
            elif s2.temperature == 16.5:
                return 0.5
            elif s2.temperature == 17:
                return 0.2
            else:
                return 0.0
        elif s1.temperature == 25:
            if s2.temperature == 25:
                return 0.9
            elif s2.temperature == 24.5:
                return 0.1
            else:
                return 0.0
        elif s1.temperature == 24.5:
            if s2.temperature == 25:
                return 0.7
            elif s2.temperature == 24.5
                return 0.3
            else:
                return 0.0
        else: #standard conditions for rest of current states when taking action "on"
            if s2.temperature == s1.temperature+0.5:
                return 0.5
            elif s2.temperature == s1.temperature+1:
                return 0.2
            elif s2.temperature == s1.temperature:
                return 0.2
            elif s2.temperature == s1.temperature-0.5:
                return 0.1
            else:
                return 0.0
    elif a == "off":
        if s1.temperature == 16:
            if s2.temperature == 16:
                return 0.9
            elif s2.temperature == 16.5:
                return 0.1
            else:
                return 0.0
        elif s1.temperature == 25:
            if s2.temperature == 25:
                return 0.3
            elif s2.temperature == 24.5:
                return 0.7
            else:
                return 0.0
        else:#standard conditions for rest of current states when taking action "off"
            if s2.temperature == s1.temperature-0.5:
                return 0.7
            elif s2.temperature == s1.temperature+0.5:
                return 0.1
            elif s2.temperature == s1.temperature:
                return 0.2
            else:
                return 0.0









from slistH import SList


class BinaryNode:

    def __init__(self, elem: object, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    def __eq__(self, other: 'BinaryNode') -> bool:
        """checks if two nodes (subtrees) are equal o not"""
        return other is not None and self.elem == other.elem and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.elem)


class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def __eq__(self, other: 'BinaryTree') -> bool:
        """checks if two binary trees are equal o not"""
        return other is not None and self._root == other._root

    def size(self) -> int:
        """Returns the number of nodes"""
        return self._size(self._root)

    def _size(self, node: BinaryNode) -> int:
        """return the size of the subtree from node"""
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def height(self) -> int:
        """Returns the height of the tree"""
        return self._height(self._root)

    def _height(self, node: BinaryNode) -> int:
        """return the height of node"""
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def preorder(self) -> None:
        """prints the preorder (root, left, right) traversal of the tree"""
        # self.draw()
        print('Preorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._preorder(self._root)
        print()

    def _preorder(self, node: BinaryNode) -> None:
        """prints the preorder (root, left, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            print(node.elem, end=' ')  # end=' ' avoid new line
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder_list(self) -> list:
        """returns a list with the preorder traversal"""
        # self.draw()
        result = []
        self._preorder_list(self._root, result)
        return result

    def _preorder_list(self, node: BinaryNode, pre_list: list) -> None:
        """populates pre_list with the preorder traversal of the subtree node"""
        if node is not None:
            pre_list.append(node.elem)
            self._preorder_list(node.left, pre_list)
            self._preorder_list(node.right, pre_list)

    def postorder(self) -> None:
        """prints the postorder (left, right, root)  traversal of the tree"""
        # self.draw()
        print('Postorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._postorder(self._root)
        print()

    def _postorder(self, node: BinaryNode) -> None:
        """prints the postorder (left, right, root) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem, end=' ')  # end=' ' avoid new line

    def postorder_list(self) -> list:
        """returns a list with the postorder traversal of the tree"""
        # self.draw()
        result = []
        self._postorder_list(self._root, result)
        return result

    def _postorder_list(self, node: BinaryNode, post_list: list) -> None:
        """populates post_list with the postorder traversal of the subtree node"""
        if node is not None:
            self._postorder_list(node.left, post_list)
            self._postorder_list(node.right, post_list)
            post_list.append(node.elem)

    def inorder(self) -> None:
        """prints the inorder (left, root, right)  traversal of the tree"""
        # self.draw()
        print('Inorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._inorder(self._root)
        print()

    def _inorder(self, node: BinaryNode) -> None:
        """prints the inorder (left, root, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._inorder(node.left)
            print(node.elem, end=' ')  # end=' ' avoid new line
            self._inorder(node.right)

    def inorder_list(self) -> list:
        """returns a list with the inorder traversal of the tree"""
        # self.draw()
        result = []
        self._inorder_list(self._root, result)
        return result

    def _inorder_list(self, node: BinaryNode, in_list: list) -> None:
        """populates in_list with the inorder traversal of the subtree node"""
        if node is not None:
            self._postorder_list(node.left, in_list)
            in_list.append(node.elem)
            self._postorder_list(node.right, in_list)

    def level_order(self) -> None:
        """prints the level order of the tree. O(n)"""
        if self._root is None:
            print('tree is empty')
        else:
            print("Level order: ", end= ' ')  # avoid the new line

            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.addLast(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                print(current.elem, end=' ')
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)

            print()

    def level_order_list(self) -> list:
        """prints the level order of the tree. O(n)"""
        result = []
        if self._root is not None:
            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.addLast(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                result.append(current.elem)
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)

        return result

    def depth(self, node):
        """ returns the depth of the node; this is the length from
        the root to the node"""
        depth_level = None

        if self._root is None:
            print('Error: the tree is empty')
        else:
            # we can use SList with tail and head
            depth_level = 0

            list_nodes = SList()
            list_nodes.addLast(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                if current == node:
                    return depth_level
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)
                depth_level += 1

        print('Not found ', node.elem)
        return None

    def draww(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draww('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draww(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draww(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draww(prefix + "     ", node.left, True)


    def draw(self):
        lines, _, _, _ = self._display_aux(self._root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.elem
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.elem
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.elem
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.elem
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

if __name__ == '__main__':
    tree = BinaryTree()

    newNode = BinaryNode(2)
    left = BinaryNode(3, newNode, None)

    right = BinaryNode(9)

    right.left = BinaryNode(8)
    right.right = BinaryNode(20)
    rrNode = right.right
    rrNode.right = BinaryNode(30)

    root = BinaryNode(5, left, right)

    tree._root = root
    tree.draw()

    print('Size of the tree:', tree.size())
    print('Height of the tree:', tree.height())
    print('root of the tree:',  tree._height(root))

    tree.preorder()
    tree.postorder()
    tree.inorder()

    print("Preorder: ", tree.preorder_list())
    print("Postorder: ", tree.postorder_list())
    print("Inorder: ", tree.inorder_list())

    tree.level_order()
    print("Level order:", tree.level_order_list())

    print('depth of root:', tree.depth(root))
    print('depth of root.left:', tree.depth(left))
    print('depth of root.right:', tree.depth(right))

