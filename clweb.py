# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 18:49:55 2012

@author: tyson
"""
import sys
import lexiabase as lb

ctxt = None
l = None

def main():
    global l
    global ctxt
    l = lb.Lexiabase()
    topmenu()

def topmenu():
    while True:
        domenu("Top", { 1:("Lexias", lexmenu),
                            2:("Links", linkmenu),
                            3:("quit", sys.exit)  })

def domenu(name, d):
    print "%s\n" % name
    for n,s in d.items():
        print "\t%d\t%s" % (n, s[0])
    r = raw_input("Choose: ")
    try:
        if r.lower() in ['q', 'quit', 'exit']:
            sys.exit()
        elif int(r) in d.keys():
            d[int(r)][1]()
        else:
            return -1
    except ValueError:
        return -1

def lexmenu():
    while True:
        domenu("Lexia", {1:("Choose Lexia.", choose_lexia),
                             2:("Edit Lexia.", edit_lexia),
                             3:("List Lexias.", list_lexias),
                             4:("New Lexia.", new_lexia),
                             5:("Top menu", topmenu) })
                             
def new_lexia():
    global l, ctxt
    n = l.new_node()
    ctxt = l[n]
    edit_lexia()

def choose_lexia():
    global l, ctxt
    while True:
        try:
            r = int(raw_input("Lexia number? "))
            ctxt = l[r]
        except ValueError:
            print "Number needed\n"
            continue
        except KeyError:
            print "Not a valid lexia.\n"
            continue
        return 0
    
def edit_lexia():
    global l, ctxt
    if ctxt:
        print "Enter lexia text:\n"
        ctxt.edit(raw_input())
    else:
        print "Need to choose a lexia."
    return 0
    
def list_lexias():
    global l, ctxt
    for n,i in l.node_iter():
        print "%d\t%s" % (n,i.preview())
    return 0


def linkmenu():
    k = -1
    while k is -1:
        k = domenu("Link", {1:("Choose Lexia to link.", choose_lexia),
                            2:("Link lexia.", link_lexia),
                            3:("Top menu.", topmenu)})

def link_lexia():
    global l,ctxt
    if not ctxt:
        print "Need to choose a lexia to link from.\n"
        return -1
    while True:
        try:
            r = int(raw_input("Lexia number to link to?"))
            l.link(ctxt.nodeid, r)
        except ValueError:
            print "Number needed.\n"
        return 0

        
if __name__ == "__main__":
    main()

        
                            
    
    