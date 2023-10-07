# -*- coding: utf-8 -*-
"""
Class Tree for Prefix Trees homework (same as usual)
+ specific display function (as in the documentation):
    - use it to display a prefix tree if you are under Ipython and managed to install Graphviz
    - otherwize use the result of print(ptree.dot_dfs(T)) online:
            https://dreampuf.github.io/GraphvizOnline
            http://www.webgraphviz.com/

"""

# General Tree class
# ------------------------------------------------------------------------------

class Tree:
    """
    Simple class for General Tree
    """

    def __init__(self, key, children=None):
        """
        Init General Tree, children is [] if not given
        """
        self.key = key
        if children is not None:
            self.children = children
        else:
            self.children = []

    @property
    def nbchildren(self):
        return len(self.children)

    
######################### Display 
# the following are just here for your tests: you cannot use them in the code you hand back


def __nodeTodot(T):
    if not T.key:
        return str(id(T)) + '[label="-"];\n'
    style = " shape = circle" if T.key[1] else ""
    return str(id(T)) + '[label="' + str(T.key[0]) + '"' + style + '];\n'
    

def __linkToDot(A, B):
    return "   " + str(id(A)) + " -- " + str(id(B)) + ";\n"


def __dot(T):
    s = ""
    for child in T.children:
        s += __nodeTodot(child)
        s += __linkToDot(T, child)    
        s += __dot(child)
    return s

def dot_dfs(T):
    s = "graph {\n"
    s += "node [shape=none margin=0 width=0.3];\n"
    s += __nodeTodot(T)
    s += __dot(T)
    s += "}"
    return s
    
def display(T):
    # Ensure all modules are available
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz.")
    # Generate dot and return display object
    dot_source = dot_dfs(T)
    display(Source(dot_source))

