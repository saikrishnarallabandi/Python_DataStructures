#!/usr/bin/python

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None	

class Tree:

	def __init__(self, name= 'root', children = None):
		self.name = name
		self.children = []

		if children is not None:
			for child in children:
				 self.add_child(child)

    def add_child(self, node):
         assert isinstance(node, Tree)
         self.children.append(node)

