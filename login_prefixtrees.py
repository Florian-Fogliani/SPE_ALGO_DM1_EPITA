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
    res=0
    if (T.key[1]) :
        res = 1
    for c in T.children :
        res += countwords(c)
    return res
    

def averagelength(T):
    """ average word length in the prefix tree T (ptree.Tree)
    return type: float
    """
    res=0
    nb_word=0
    for c in T.children :
        (len,nb) = __average__(c,1)
        res += len
        nb_word += nb
    return res/nb_word if nb_word != 0 else 0

def __average__(T,level):
    """ average depend on the level
    return type : tuple
    """
    res=0
    nb_word = 0
    if (T.key[1]):
        res += level
        nb_word+=1
    for c in T.children :
        (len,nb) = __average__(c,level+1)
        res += len
        nb_word += nb
    return (res,nb_word)
    

###############################################################################
## Search and list

def wordlist(T):
    """ generate the word list, in alphabetic order, of the prefix tree T (ptree.Tree)
    return type: str list
    """
    res = []
    if (T.key[1]):
        res += [[T.key[0]]]
    for c in T.children : 
        for w in wordlist(c):
            word = T.key[0]
            for l in w:
                word+= l
            res += [word]
                   
    return res        


def longestword(T):
    """ search for the longest word in the prefix tree T (ptree.Tree)
    return type: str    
    """
    words = wordlist(T)
    if (len(words) == 0):
        return ""
    return max(words,key=len)
    


def searchword(T, w):
    """ search for the word w (str) not empty in the prefix tree T (ptree.Tree)
    return type: bool
    """
    if (T.key[0] == '') :
        for c in T.children : 
            if (searchword(c,w)):
                return True
    else :
        if (len(w) == 1 and T.key[0]==w):
            return True
        for c in T.children :
            if (searchword(c,w[1:])):
                return True
    return False
    

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
