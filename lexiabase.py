import linkbase as lkb

class Lexiabase(lkb.Linkbase):
  def __init__(self):
	super(Lexiabase,self).__init__(Lexia)
  def version_link(self, younger, elder):
	pass
  def new_version(self, nid):
	newnid = self[nid].copy()
	self.replace(nid,newnid)
	self.link(newnid, nid, VersionLink())
	return newnid
  def make_composite(self, basenode, lautres):
	for n,i in enumerate(lautres):
	  self.link(basenode, i, CompositeLink(n).out())
  

class Lexia (lkb.LinkNode):
  def __repr__(self):
	return "<<LEX::%d::%s>>" % (self.nodeid, self.contents[:25])
  def predicate(self, arg):
	return self.contents.find(arg) > 0
  def thetext(self):
	lb = self.base
	links = lb.links_to(self.nodeid, "type", "composite")
	s = sorted(links, lambda n: lb.get_edge_tags(self.nodeid, n)["priority"])
	cts = self.contents
	for i in s:
	  cts += lb[i].thetext()
	return cts
