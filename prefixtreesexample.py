from algo_py import ptree


"""
do not import this file in your login_prefixtrees.py 
-> this would prevent your code to be tested :(
only use it for your tests!
"""

################################################################################
## tree built with "textFiles/wordList1.txt"

Tree1 = ptree.Tree(('', False),
             [ptree.Tree(('c', False),
                   [ptree.Tree(('a', False),
                         [ptree.Tree(('s', False),
                               [ptree.Tree(('e', True)),
                                ptree.Tree(('t', True),
                                     [ptree.Tree(('l', False),
                                           [ptree.Tree(('e', True))])])])]),
                    ptree.Tree(('i', False),
                         [ptree.Tree(('r', False),
                               [ptree.Tree(('c', False),
                                     [ptree.Tree(('l', False),
                                           [ptree.Tree(('e', True))])])]),
                          ptree.Tree(('t', False),
                               [ptree.Tree(('y', True))])]),
                    ptree.Tree(('o', False),
                         [ptree.Tree(('m', False),
                               [ptree.Tree(('e', True))]),
                          ptree.Tree(('u', False),
                               [ptree.Tree(('l', False),
                                     [ptree.Tree(('d', True))])])])]),
        ptree.Tree(('f', False),
             [ptree.Tree(('a', False),
                   [ptree.Tree(('m', False),
                         [ptree.Tree(('e', True)),
                          ptree.Tree(('o', False),
                               [ptree.Tree(('u', False),
                                     [ptree.Tree(('s', True))])])]),
                    ptree.Tree(('n', True),
                         [ptree.Tree(('c', False),
                               [ptree.Tree(('y', True))])])])])])
                        
