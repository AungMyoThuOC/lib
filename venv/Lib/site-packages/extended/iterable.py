def tally(expr, test=lambda x:x):
    """
    tallies all items in expr using test as the criteria.  The default test is none; just
    tally the items in the list.

    Parameters
    ----------
    expr : list
        list of items to be tallied
    test : function
        test to be applied to each item to determine if the items are tallied together
    
    Returns
    -------
    out : list
        list of lists with the items tallied up.  If you use a nested list,
        the items get returned as a tuple.  If you use a dictionary, you'll
        only get the keys.  
    
    Examples
    --------
    >>> xt.tally(['a','a','b','a','c','b','a'])
    [['a', 4], ['b', 2], ['c', 1]]
    
    >>> # you can use objects as tallied items
    >>> import sympy as sp
    >>> sp.var('a b c')
    >>> xt.tally([a,a,b,a,c,b,a])
    [[a, 4], [b, 2], [c, 1]]
    
    >>> # if you nest in a list, it gets returned as a tuple
    >>> xt.tally([[1,2],[3,4],[3,4]])
    [[(1, 2), 1], [(3, 4), 2]]

    >>> # numpy arrays behave just like lists
    >>> xt.tally([np.array([1,2]),np.array([3,4]),np.array([1,2])])
    [[(1, 2), 2], [(3, 4), 1]]
        
    
    >>> # tests of items return just the 
    >>> xt.tally([[1,2],[2,3],[1,2],[1,1]],test=xt.first)
    [[(1, 2), 3], [(2, 3), 1]]
    
    >>> # it's not recommended to use on dicts or sets or other unordered collections
    >>> # as elements since the order upon exit cannot be guaranteed. Turn these 
    >>> # into lists first
    >>> xt.tally([{'a','b','c'}])
    [[('b', 'c', 'a'), 1]]
    """

    D = {} #stores the tallies
    E = {} #stores the test definitions
    for i in expr:
        try:
            iter(i)
        except:
            pass
        else:
            if not isinstance(i,str):
                i = tuple(i)
        try:
            D[test(i)]+=1
        except KeyError:
            E[test(i)] = i
            D[test(i)] = 1           
    return [[E[k],v] for k,v in D.items()]


def counts(expr):
    """
    returns a count of each item in the list as a dict

    Parameters
    ----------
    expr : iterable
        the list with elements that need tallied.

    Returns
    -------
    out : dict
        the keys are the items and the values are the counts

    >>> xt.counts(['a','a','b','a','c','b','a'])
    {'a': 4, 'b': 2, 'c': 1}
    
    >>> # you can use objects as tallied items
    >>> import sympy as sp
    >>> sp.var('a b c')
    >>> xt.counts([a,a,b,a,c,b,a])
    {a: 4, b: 2, c: 1}
    
    >>> # if you nest in a list, it gets returned as a tuple
    >>> xt.counts([[1,2],[3,4],[3,4]])
    {(1, 2): 1, (3, 4): 2}

    >>> # numpy arrays behave just like lists
    >>> xt.counts([np.array([1,2]),np.array([3,4]),np.array([1,2])])
    {(1, 2): 2, (3, 4): 1}
        
    >>> # it's not recommended to use on dicts or sets or other unordered collections
    >>> # as elements since the order upon exit cannot be guaranteed. Turn these 
    >>> # into lists first
    >>> xt.counts([{'a','b','c'}])
    {('c', 'b', 'a'): 1}

    """
    return {k:v for k,v in tally(expr)}


def counts_by(expr, test=lambda x:x):
    """
    returns a count of each item in the list as a dict

    Parameters
    ----------
    expr : iterable
        the list with elements that need tallied.

    Returns
    -------
    out: dict
        the keys are the items and the values are the counts

    >>> xt.counts_by(['a','a','b','a','c','b','a'])
    {'a': 4, 'b': 2, 'c': 1}
    
    >>> # you can use objects as tallied items
    >>> import sympy as sp
    >>> sp.var('a b c')
    >>> xt.counts_by([a,a,b,a,c,b,a])
    {a: 4, b: 2, c: 1}
    
    >>> # if you nest in a list, it gets returned as a tuple
    >>> xt.counts_by([[1,2],[3,4],[3,4]])
    {(1, 2): 1, (3, 4): 2}

    >>> # numpy arrays behave just like lists
    >>> xt.counts_by([np.array([1,2]),np.array([3,4]),np.array([1,2])])
    {(1, 2): 2, (3, 4): 1}
        
    
    >>> # tests of items return just the first item that satisfies the condition
    >>> xt.counts_by([[1,2],[2,3],[1,2],[1,1]],test=xt.first)
    {(1, 2): 3, (2, 3): 1}
    
    >>> # it's not recommended to use on dicts or sets or other unordered collections
    >>> # as elements since the order upon exit cannot be guaranteed. Turn these 
    >>> # into lists first
    >>> xt.counts_by([{'a','b','c'}])
    {('c', 'b', 'a'): 1}

    """
    return {k:v for k,v in tally(expr, test=test)}
    


def group_by(expr, test=lambda x:x, reduce =lambda x:x):
    """
    groups the items in the list based upon the keys

    Parameters
    ----------
    expr : iterable
        list of items to be grouped by
    test : function or dict, optional
        fn to apply to each item to tell if they should be grouped together. if
        dict, then it's that function and the key is the function to be applied
        to each member of the output
    reduce: function, optional
        function to apply to the final lists 

    Returns
    -------
    dict
        keys of the groupings and the items from the original list to be together

    Examples
    --------
    
    >>> xt.group_by(['a1','b2','c3','a2','b1','c1'],test = xt.first)
    {'a': ['a1', 'a2'], 'b': ['b2', 'b1'], 'c': ['c3', 'c1']}
    
    >>> xt.group_by(['a1','b2','c3','a2','b1','c1'],test = {xt.first:xt.last})
    {'a': ['1', '2'], 'b': ['2', '1'], 'c': ['3', '1']}
    
    >>> xt.group_by(['a1','b2','c3','a2','b1','c1'],test = {xt.first:xt.last},
    >>>        reduce = lambda x:''.join(x))
    {'a': '12', 'b': '21', 'c': '31'}

    """
    D = {}
    if isinstance(test, dict):
        test, final = list(test.items())[0]
    else:
        assert callable(test)
        final = lambda x:x
    for i in expr:
        try:
            iter(i)
        except:
            pass
        else:
            if not isinstance(i,str):
                i = tuple(i)
        try:
            D[test(i)] += [final(i)]
        except KeyError:
            D[test(i)] = [final(i)]           
    return {k:reduce(v) for k,v in D.items()}


def gather_by(expr, test = lambda x: x):
    """
    gathers the items in the list by the tests, which can be nested    

    Parameters
    ----------
    expr : iterable
        list of things to be gathered
    test : function or list, optional
        the test (or for nesting, tests) that should be applied to gather at
        each level

    Returns
    -------
    list
        list (or list of lists) gathered at each level by the test(s)

    Examples
    --------

    >>> xt.gather_by(['a1','b2','a1','a2','b1','b2'],test = xt.first)
    [['a1', 'a1', 'a2'], ['b2', 'b1', 'b2']]
    
    >>> xt.gather_by(['a1','b2','a1','a2','b1','b2'],test = [xt.first,xt.last])
    [[['a1', 'a1'], ['a2']], [['b2', 'b2'], ['b1']]]

    """
    try: iter(test)
    except: test = [test]
    
    if len(test) == 1:
        return list(group_by(expr,test[0]).values())
    else:
        return [gather_by(i,test[1:]) for i in list(group_by(expr,test[0]).values())]



