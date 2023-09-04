import os
cmd = "dot -Tpng avlTree.dot -o avlTree.png"

class treeNode(object):
	def __init__(self, name):
		value = 0
		for character in name:
			value += ord(character)
		self.value = value
		self.name = name
		self.l = None
		self.r = None
		self.h = 1

class AVLTree(object):

	def toInt(self, name):
		value = 0
		for character in name:
			value += ord(character)
		return value

	def insert(self, root, key):

		if not root:
			return treeNode(key)
		elif self.toInt(key) < root.value:
			root.l = self.insert(root.l, key)
		else:
			root.r = self.insert(root.r, key)

		root.h = 1 + max(self.getHeight(root.l),
						self.getHeight(root.r))

		b = self.getBal(root)

		if b > 1 and self.toInt(key) < root.l.value:
			return self.rRotate(root)

		if b < -1 and self.toInt(key) > root.r.value:
			return self.lRotate(root)

		if b > 1 and self.toInt(key) > root.l.value:
			root.l = self.lRotate(root.l)
			return self.rRotate(root)

		if b < -1 and self.toInt(key) < root.r.value:
			root.r = self.rRotate(root.r)
			return self.lRotate(root)

		return root

	def lRotate(self, z):

		y = z.r
		T2 = y.l

		y.l = z
		z.r = T2

		z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
		y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

		return y

	def rRotate(self, z):

		y = z.l
		T3 = y.r

		y.r = z
		z.l = T3

		z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
		y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.h

	def getBal(self, root):
		if not root:
			return 0

		return self.getHeight(root.l) - self.getHeight(root.r)

	def preOrder(self, root):

		if not root:
			return

		self.preOrder(root.l)
		print("{0} ".format(root.value), end="")
		self.preOrder(root.r)

	def export_graphviz(self, root):
		dotContent = "digraph G {\n" + self.aux_export_graphviz(root) + "}"
		f = open("avlTree.dot", "w")
		f.write(dotContent)
		f.close()
		os.system(cmd)

	def aux_export_graphviz(self, root):
		if not root:
			return
		rootNode = "node{0}".format(root.value) + \
			"[label=\"{0}-{1}\"]\n".format(root.value, root.name)
		value = rootNode + "\n"

		leftNode = self.aux_export_graphviz(root.l)
		rightNode = self.aux_export_graphviz(root.r)

		if root.l:
			value += "node{0}".format(root.value) + \
				" -> node{0}\n".format(root.l.value) + leftNode
		if root.r:
			value += "node{0}".format(root.value) + \
				" -> node{0}\n".format(root.r.value) + rightNode

		return value

Tree = AVLTree()
root = None

root = Tree.insert(root, "hola")
root = Tree.insert(root, "adios amor")
root = Tree.insert(root, "casa")
root = Tree.insert(root, "perro")
root = Tree.insert(root, "gato")
root = Tree.insert(root, "casa1")
root = Tree.insert(root, "casa2")
root = Tree.insert(root, "casa3")
root = Tree.insert(root, "casa1")

# Preorder Traversal
print("Preorder traversal of the",
	"constructed AVL tree is")
Tree.preOrder(root)
print()

Tree.export_graphviz(root)

#https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
#https://favtutor.com/blogs/avl-tree-python