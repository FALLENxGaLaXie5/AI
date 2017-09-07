# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:01:48 2017

@author: joshua.steward095
"""

from collections import deque

#-----------------------------------------------------------
# graph code
#-----------------------------------------------------------
class Vertex(object):
	def __init__( self, label=None, value=1 ):
		self.label = label
		self.value = value
		self.edge_list = list()
		self.visited = False
		self.explored = False
	def __eq__(self, other):
		return self.label == other.label
	def __gt__(self, other):
		return self.value > other.value

	def Connect(self, v, w=1):	self.edge_list.append((v,w))
	def EdgeIterator(self):		return iter(self.edge_list)
	def SetVisited(self):		self.visited = True
	def GetVisited(self):		return self.visited
	def SetExplored(self):		self.explored = True
	def GetExplored(self):		return self.explored
	def SetLabel(self, label):	self.label = label
	def GetLabel(self):			return self.label
	def SetValue(self, value):	self.value = value
	def GetValue(self):			return self.value

#-----------------------------------------------------------
class Graph(object):
	def __init__(self, directed):
		self.vertices = {}
		self.directed = directed
		self.start_vertex = None
		self.goal_vertex = None

	def AddVertex( self, vertex ):
		self.vertices[vertex.GetLabel()] = vertex
	def GetVertex( self, vertex_label ):
		return self.vertices[vertex_label]
	def AddEdge( self, v1, v2, w = 1 ):
		v1label = v1.GetLabel()
		v2label = v2.GetLabel()
		if v1label in self.vertices and v2label in self.vertices:
			self.vertices[v1label].Connect(self.vertices[v2label], w)
			if not self.directed:
				self.vertices[v2label].Connect(self.vertices[v1label], w)
	def ResetVertices( self ):
		for vertex_label in self.vertices:
			self.vertices[vertex_label].visited = False
			self.vertices[vertex_label].explored = False
	def SetStartVertex( self, start ):
		self.start_vertex = start
	def GetStartVertex( self ):
		return self.start_vertex
	def SetGoalVertex( self, goal ):
		self.goal_vertex = goal
	def GetGoalVertex( self ):
		return self.goal_vertex
		
#-----------------------------------------------------------
# SearchTree code			
#-----------------------------------------------------------
class Node(object):
	def __init__( self, vertex ):
		self.vertex = vertex
		self.label = vertex.GetLabel()
		self.parent = None
		self.children = list()
		self.fcost = 0
		self.level = 0
	def __eq__(self, other):
		return self.label == other.label
	def __lt__(self, other):
		return self.fcost < other.fcost
								
	def ChildIterator(self):		return iter(self.children)
	def GetParent( self ):		return self.parent
	def GetLabel( self ):		return self.label
	def GetVertex( self ):		return self.vertex
	def GetCost( self ):			return self.fcost
	def PrintParents( self ):
		print()
		node = self
		while (node):
			print(node.GetLabel())
			node = node.GetParent()
		
#-----------------------------------------------------------
class SearchTree(object):
	def __init__(self, root):
		self.nodes = list()
		self.root = root
		self.root.level = 0

	def GetRoot( self ):			return self.root
			
	def AddChildNode( self, pnode, cnode ):	
		self.nodes.append(cnode)
		cnode.parent = pnode
		pnode.children.append(cnode)

	def Reset( self ): self.nodes[:] = []
	
	def PrintTree( self ):
		frontier = deque()	
		frontier.append(self.root)
		
		current_level = 0
		while frontier:
			pnode = frontier.popleft()
			
			if current_level != pnode.level:
				print(' ')
				current_level = pnode.level
			if pnode.GetParent():	
				print(pnode.GetLabel(),'[', pnode.GetParent().GetLabel(),']', '=', pnode.fcost, '  ', end="", flush=True)
			else:
				print(pnode.GetLabel(),'[]', '=', pnode.fcost, '  ', end="", flush=True)

			children = pnode.ChildIterator()
			for child in children:
				child.level = current_level+1
				frontier.append(child)
		
		print()