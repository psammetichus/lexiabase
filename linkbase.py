import networkx
from random import randrange

class Linkbase (object):
  def __init__(self, objctor):
	self.store = networkx.digraph.DiGraph()
	self.index = {}
	self.ctor = objctor
	self.counter = 0
  def __getitem__(self, x):
	return self.index[x]
  def __setitem__(self, x, y):
	self.index[x] = y
	self.store.add_node(y)
  def new_node(self, contents):
	n = self.counter
	b = self.ctor(contents, self, n)
	self[n] = b
	self.counter+=1
	return n
  def link(self, lid1, lid2, linktypeobj=None):
	if not linktype:
	  self.store.add_edge(lid1, lid2)
	else:
	  self.store.add_edge(lid1, lid2, linktypeobj.out())
  def links_to(self, nodeid, linktype):
	return [l for l in filter(lambda x:
		self.store.get_edge_data(n,x)["type"] == linktype,
		self.store.neighbors[nodeid])]
  def search(self, squery):
	ls = []
	for l in self.index.keys():
		if self[l].predicate(squery):
		  ls.append(l)
	return ls
  def vacuum(self):
	for i in self.index.keys():
	  n = self[i]
	  if n.is_empty() and self.store.out_degree(n) == 0:
		self.store.remove_node(n)
		del self.index[i]
  def replace(self, old, new):
	s = self.store
	for i in s.in_edges(old):
	  d = s.get_edge_data(i,old)
	  s.remove_edge(i,old)
	  s.add_edge(i,new,d)
	return o.nodeid
  def get_edge_tags(self, m, n):
	return self.store.get_edge_data(m, n)
  def remove_node(self, nodeid):
	self.store.remove_node(nodeid)
	del self.index[nodeid]
  def _unoccupied_nodeid(self, n):
	return self.index.has_key(n)
  def _random_new_id(self):
	while True:
	  i = randrange(0, 2**32-1)
	  if self._unoccupied_nodeid(i):
		return i
	  

class LinkNode(object):
	def __init__(self, data, base, nodeid):
		self.contents = data
		self.base = base
		self.nodeid = nodeid
	def links_to(self):
	  return [self.base[i] for i in self.base.links_to(self.nodeid)]
	def predicate(self, arg):
	  return self.contents is arg
	def edit(self, newdata):
	  self.contents = newdata
	def is_empty(self):
	  return len(self.contents) > 0
	def copy(self):
	  return self.base.new_node(self.contents)
	def link(self, lautre, linktype=None):
	  self.base.link(self.nodeid, lautre.nodeid, linktype)
	
class Linktype(object):
  def __init__(self, ltype):
	self.ltype = ltype
	self.params = {}
  def _update_params(self, **kwargs):
	self.params.update(kwargs)
  def out(self):
	op = {"type":self.ltype}
	op.update(self.params)
	return op

class VersionLink(Linktype):
  """links toward nodes that are younger"""
  def __init__(self):
	super(VersionLink,self).__init__("version")

class CompositeLink(Linktype):
  """links toward nodes that should be considered part of a composite node"""
  #not recursive; avoid cycles
  def __init__(self, priority):
	super(CompositeLink,self).__init__("composite")
	self._update_params(priority=priority)

class ThreadLink(Linktype):
  def __init__(self, name):
	super(ThreadLink,self).__init__("thread")
	self._update_params(threadname=name)
