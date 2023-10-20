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
    if (len(w) == 1):
        for c in T.children :
            if c.key[0] == w and c.key[1]:
                return True
        return False
    if (T.key[0] == ''):
        for c in T.children :
            if (c.key[0] == w[0]):
                if (searchword(c,w[1:])):
                    return True
    else:
        for c in T.children :
            if (c.key[0] == w[0]):
                if (searchword(c,w[1:])):
                    return True
    return False
            
    

def hangman(T, pattern):
    """ Find all solutions for a Hangman puzzle in the prefix tree T: 
        words that match the pattern (str not empty) where letters to fill are replaced by '_'
    return type: str list
    """
    res=[]
    for c in T.children :
        if (c.key[0] == pattern[0] or pattern[0] == "_"):
            res  += __hangman_bis__(c,pattern)
    return res

def __hangman_bis__(T,pattern):
    """ Find all solutions for a Hangman puzzle in the prefix tree T: 
        words that match the pattern (str not empty) where letters to fill are replaced by '_'
    return type: str list
    """
    res=[]
    if (len(pattern)==1):
        if ((T.key[0] == pattern or pattern == "_") and T.key[1]):
            res.append(T.key[0])
    if (len(pattern) >= 2):
        for c in T.children :
            if (c.key[0] == pattern[1] or pattern[1] == "_"):
                res_c = __hangman_bis__(c,pattern[1:])
                for r in res_c:
                    res.append(T.key[0] + r)
    return res
                
    
        
            



###############################################################################
## Build

def buildlexicon(T, filename):
    """ save the tree T (ptree.Tree) in the new file filename (str)
    """
    file = open(filename,'x')
    words = wordlist(T)
    for w in words :
        file.write(w+"\n")
    file.close()

def __get_key__(T):
    """get a key of a tree
    return : the char of the key
    """
    return T.key[0]

def __sort__tree__(T):
    """trie the tree selon les clés char des enfants
    return : rien du tout car en place"""
    T.children.sort(key=__get_key__)
    for c in T.children:
        __sort__tree__(c)
        

def addword(T, w):
    """ add the word w (str) not empty in the tree T (ptree.Tree)
    """
    __sort__tree__(T)
    boucle=True
    i=0
    if (searchword(T,w)):
        return
    while (boucle):
        if (T.children == None):
            boucle=False
        long = len(T.children)
        r=0
        for y in range(long):
            if (T.children[y].key == w[i]):
                i+=1
                T=T.children[y]
                break
            r+=1
        if (r == long):
            boucle=False        
    T.children.append(__word_creator__(w[i:]))
           
def __word_creator__(word):
    """Create a tree with word 
    return type : ptree Tree
    """
    if (len(word)==0):
        return []
    if (len(word)==1):
        tree = ptree.Tree((word[0],True))
    else :
        tree = ptree.Tree((word[0],False),[__word_creator__(word[1:])])
    return tree

def buildtree(filename):
    """ build the prefix tree from the lexicon in the file filename (str)
    return type: ptree.Tree
    """
    file = open(filename,'r')
    words = file.readlines()
    words.sort()
    tree = ptree.Tree(('',False))
    for w in words:
        addword(tree,w.strip("\n"))
    return tree
      
