def nest_while_list(f,expr,test,m=1,max_iter=None, n=0):
    """
    
    repeatedly applies f to expr until test yields False

    Parameters
    ----------
    f : function
        function to apply each time.
    expr : any
        starting expression.
    test : function
        test to continue applying f.
    m : int, optional
        if int: equivalent to [m,m]; if list: [m_min,m_last], Do the first 
        m_min iterations even if Test is False, and use last m_last as a list 
        for results for test.
    max_iter : int, optional
        iterates a maximum of max_iter number of times. The default is 1024.
    n : int, optional
        applies test n additional times after the completion. The default is 0.

    Returns
    -------
    out : list
        returns list of results for successive applications of f to expr
        
    Examples
    --------
    
    >>> xt.nest_while_list(lambda x:x/2, 123456, xt.even_q)
    [123456, 61728.0, 30864.0, 15432.0, 7716.0, 3858.0, 1929.0]

    >>> xt.nest_while_list(lambda x:x/2, 123456, xt.even_q, m=[7,1], n=1)
    [123456, 61728.0, 30864.0, 15432.0, 7716.0, 3858.0, 1929.0, 964.5, 482.25]

    >>> #The collatz conjecture with 19 as the starting point:
    >>> xt.nest_while_list(lambda x:[x//2,3*x+1][x%2], 19, lambda x: x!=1)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    L = [expr]
    i = 0
    try:
        iter(m)
    except:
        o=m
    else:
        m,o = m
    finally:
        assert isinstance(m,int)
    if max_iter and m:
        assert m < max_iter
    while ((test(*L[-o:]) if o else test(expr)) and
           (i < max_iter if max_iter else True)) or i<m:
        expr = f(expr)
        L.append(expr)
        i += 1
    if n>0:
        for i in range(n):
            expr = f(expr)
            L.append(expr)
    elif n<0:
        L=L[:n]
    return L
    

def nest_while(f,expr,test,m=1,max_iter=None, n=0):
    """
    
    repeatedly applies f to expr until test yields False

    Parameters
    ----------
    f : function
        function to apply each time.
    expr : any
        starting expression.
    test : function
        test to continue applying f.
    m : int, optional
        if int: equivalent to [m,m]; if list: [m_min,m_last], Do the first 
        m_min iterations even if Test is False, and use last m_last as a list 
        for results for test.
    max_iter : int, optional
        iterates a maximum of max_iter number of times. The default is 1024.
    n : int, optional
        applies test n additional times after the completion. The default is 0.

    Returns
    -------
    out : item
        returns results for successive applications of f to expr
        
    Examples
    --------
    
    >>> xt.nest_while(lambda x:x/2, 123456, xt.even_q)
    1929.0

    >>> xt.nest_while(lambda x:x/2, 123456, xt.even_q, m=[7,1], n=1)
    482.25

    """
    L = [expr]
    i = 0
    try:
        iter(m)
    except:
        o=m
    else:
        m,o = m
    finally:
        assert isinstance(m,int)
    #check if we need to do the list in the first place
    if m==1 and o==1 and n==0:
        while (test(expr) and (i < max_iter if max_iter else True)) or i<m:
            expr = f(expr)
            i += 1
        return expr
    else:
        #you need the max iter to be larger or equal to m (minimum iterations)
        if max_iter and m:
            assert m <= max_iter
        #the main loop
        while (test(*L[-o:]) and
               (i < max_iter if max_iter else True)) or i<m:
            expr = f(expr)
            L.append(expr)
            L=L[min([o,n,-1])-1:]
            i += 1
        #if you need additional looping
        if n>0:
            for i in range(n):
                expr = f(expr)
                L.append(expr)
                L=L[len(L)+min([o,n,-1])-1:]
        if n<0:
            return L[n-1]
        else:
            return L[-1]

def nest(f, expr, n):
    """
    returns the value of f applied to expr n times

    Parameters
    ----------
    f : function
        function to be applied.
    expr : any
        expression f is to be applied to.
    n : int
        number of times.

    Returns
    -------
    expr : any
        result of f(f(f(....expr ...))) nested n deep

    Examples
    --------
    >>> xt.nest(lambda x: x/10, 123456, 4)
    12.3456

    >>> xt.nest(xt.first, [['a','b'],['c','d']], 2)
    'a'
    """
    for i in range(n):
        expr = f(expr)
    return expr

            
def nest_list(f, expr, n):
    """
    returns the list of results of applying f to expr n times

    Parameters
    ----------
    f : function
        function to be applied.
    expr : any
        what function is to be applied to.
    n : int
        number of times f is to be applied.

    Returns
    -------
    out : list
        returns [f(expr), f(f(expr)), f(f(f(expr))), ...]

    Examples
    --------
    
    >>> xt.nest_list(lambda x:x//2, 1024, 10)
    [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    
    >>> xt.nest_list(lambda x:x[0], [['a','b'],['c','d']], 2)
    [['a', 'b'], 'a']

    """
    end = []
    for i in range(n):
        expr = f(expr)
        end.append(expr)
    return end














