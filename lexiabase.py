import linkbase as lkb

class Lexiabase(lkb.Linkbase):
  def __init__(self):
    super(Lexiabase,self).__init__(Lexia)
  def new_version(self, nid):
    newnid = self[nid].copy()
    self.replace(nid,newnid)
    self.link(newnid, nid, LINK_T_VERSION)
    return newnid
  def make_composite(self, basenode, lautres):
    self.store.add_path([basenode]+lautres, ltype=LINK_T_COMPOSE)
  def new_tag(self, nodeid, tagnodeid):
      self.link(tagnodeid, nodeid, LINK_T_TAG)
  def get_tags(self):
      return [u for (u,v,d) in self.store.edges_iter(data=True) if d['ltype']==LINK_T_TAG]

LINK_T_N = 0
LINK_T_TAG=3
LINK_T_VERSION=1
LINK_T_COMPOSE=2
LINK_T_AMONG_TAGS = 3

class Lexia (lkb.LinkNode):
  def __repr__(self):
    return "<<LEX::%d::%s>>" % (self.nodeid, self.contents[:25])
  def predicate(self, arg):
    return self.contents.find(arg) > 0
#  def thetext(self):
#    lb = self.base
#    links = lb.links_to(self.nodeid, LINK_T_COMPOSE)
#    
#    cts = self.contents
#    for i in s:
#      cts += lb[i].thetext()
#    return cts
