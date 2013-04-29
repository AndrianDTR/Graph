#! /usr/bin/env python

class GraphExc(Exception):
	def __init__(self, msg):
		self.msg = "Error! " + msg
	
	def __str__(self):
		return self.msg
		
class GraphNode(object):
	arcs = []
	name = ''
	def __init__(self, name):
		self.arcs = []
		self.name = name
	
	def __str__(self):
		return self.name
	
	def __repr__(self):
		return self.name

	def getArcs(self):
		return self.arcs
		
	def addArc(self, node):
		self.arcs.append(node)
		return node
	
	def delArc(self, node):
		if not node in self.arcs:
			raise GraphExc("This node is not linked with node '{}'.".node.name)
		self.arcs.remove(node)
	
	def dump(self, prefix):
		for arc in self.arcs:
			print "{}{} -> {}".format(prefix, self.name, arc.name)

class Graph:
	def __init__(self):
		self.nodes = []
		
	def __getitem__(self, node):
		if isinstance(node, GraphNode):
			if not node in self.nodes:
				raise GraphExc("Specified node is not in graph.")
			return node
		else:
			nodeMap = dict([(el.name, el) for el in self.nodes])
			res = nodeMap.get(node, None)
			return res
		
	def addNode(self, nodes):
		if isinstance(nodes, list):
			for node in nodes:
				self.nodes.append(node)
		else:
			self.nodes.append(nodes)
		return nodes
		
	def delNode(self, node):
		if not node in self.nodes:
			raise GraphExc("This node is not in graph.")
		self.nodes.remove(node)
	
	def dump(self):
		prefix = ''
		for node in self.nodes:
			node.dump(prefix + ' ')
	
	def getSiblings(self, node):
		if not node in self.nodes:
			raise GraphExc("This node is not in graph.")
		return node.getArcs()
	
	def getParents(self, node):
		if not node in self.nodes:
			raise GraphExc("This node is not in graph.")
		return [parent for parent in self.nodes if node in parent.getArcs()]
	

graph = Graph()
a = graph.addNode(GraphNode("A"))
b = graph.addNode(GraphNode("B"))
c = graph.addNode(GraphNode("C"))
d = graph.addNode(GraphNode("D"))
e = graph.addNode(GraphNode("E"))
f = graph.addNode(GraphNode("F"))

a.addArc(a)
a.addArc(c)
b.addArc(c)
b.addArc(d)
c.addArc(d)
d.addArc(c)
e.addArc(f)
f.addArc(c)

print b in graph[a].getArcs()
print b in graph['A'].getArcs()
graph.dump()
print graph.getSiblings(b)
print graph.getParents(c)
