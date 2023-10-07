__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2023-10-03'

"""
Prefix Trees homework
2023-10 - S3
@author: login
"""

from algo_py import ptree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

##############################################################################
## Measure

def countwords(T):
    """ count words in the prefix tree T (ptree.Tree)
    return type: int
    """
    
    #FIXME
    pass
    

def averagelength(T):
    """ average word length in the prefix tree T (ptree.Tree)
    return type: float
    """
    
    #FIXME
    pass
    

###############################################################################
## Search and list

def wordlist(T):
    """ generate the word list, in alphabetic order, of the prefix tree T (ptree.Tree)
    return type: str list
    """
    
    #FIXME
    pass


def longestword(T):
    """ search for the longest word in the prefix tree T (ptree.Tree)
    return type: str    
    """
    
    #FIXME
    pass


def searchword(T, w):
    """ search for the word w (str) not empty in the prefix tree T (ptree.Tree)
    return type: bool
    """
    
    #FIXME
    pass
    

def hangman(T, pattern):
    """ Find all solutions for a Hangman puzzle in the prefix tree T: 
        words that match the pattern (str not empty) where letters to fill are replaced by '_'
    return type: str list
    """
    #FIXME
    pass


###############################################################################
## Build

def buildlexicon(T, filename):
    """ save the tree T (ptree.Tree) in the new file filename (str)
    """
    
    #FIXME
    pass


def addword(T, w):
    """ add the word w (str) not empty in the tree T (ptree.Tree)
    """
    
    #FIXME
    pass


def buildtree(filename):
    """ build the prefix tree from the lexicon in the file filename (str)
    return type: ptree.Tree
    """
    
    #FIXME
    pass   
