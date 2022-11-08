def printr(expr):
    """
    Prints out an expression and returns it as well for inline diagnosis.
    You shouldn't use print to debug, but it's not like you're going to stop.
    
    Parameter + Return
    ------------------
    expr : any
        item to be analyzed/returned

    Example
    -------
    >>> #Use it within a comprehension to diagnose problems.
    >>> #If you just use print, the result would be [None,None,None,None]
    >>> [xt.printr(i)**3 for i in range(4)]
    0
    1
    2
    3
    [0, 1, 8, 27]
    
    
    
    """
    print(expr)
    return expr


def check(f, fail_f=lambda: None, name=None):
    """
    trys to evaluate the function

    Parameters
    ----------
    f : fn
        function to by tried. Must be in a callable format (either a no-arg def 
        function or lambda:)
    fail_f : fn, optional
        fallback. The default is to return none.
    name : Error
        limit fallback to named error type, e.g. TypeError or KeyError.  No quotes.

    Returns
    -------
    f() or fail_f() or None: any
        returns whatever the successful execution is, f or fail_f else None.
    
    Examples
    --------
    
    >>> #check if an item is in a dictionary, should throw a KeyError otherwise
    >>> d = {1:'a',2:'b',3:'c'}
    >>> [xt.check(lambda: d[i], lambda: i) for i in range(1,5)]
    ['a', 'b', 'c', 4]
    
    >>> #Or you can ignore the failues and just return None for filtering later
    >>> [xt.check(lambda: d[i]) for i in range(1,5)]
    ['a', 'b', 'c', None]

    >>> [xt.check(lambda: d[i], lambda: i, KeyError) for i in range(1,5)]
    ['a', 'b', 'c', 4]
    
    >>> [xt.check(lambda: d[i], lambda: i, TypeError) for i in range(1,5)]   
    KeyError: 4
    """
    if name is None:
        try: return f()
        except: return fail_f()
    else:
        try: return f()
        except name: return fail_f()
            


