"""
Base class for attributed graphs.

"""
import networkx as nx


class aGraph(nx.Graph):

	def __init__(self, G=None, data=None, behavior_model):
		super(aGraph,self).__init__(G)
		self.data = data
		self.bm = behavior_model