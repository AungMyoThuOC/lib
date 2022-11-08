def even_q(expr):
    """
    Returns True if number is even else returns False

    Parameters
    ----------
    expr : numeric
        number to be tested

    Returns
    -------
    out : bool
        True if divisible by 2, False otherwise.

    Examples
    --------
    >>> xt.even_q(2)
    True    

    >>> xt.even_q(1)
    False
    
    >>> # a departure from wolfram, even_q works for floats 
    >>> xt.even_q(2.0)
    True
    
    >>> # even_q works for non-integer numbers, returns false
    >>> xt.even_q(0.4)
    False
    
    >>> # it even works on lists
    >>>> xt.even_q(range(5))
    [True, False, True, False, True]
    """
    try:
        iter(expr)
    except:
        return expr%2==0
    else:
        return [even_q(i) for i in expr]

def odd_q(expr):
    """
    Returns True if number is odd else returns False

    Parameters
    ----------
    expr : numeric
        number to be tested

    Returns
    -------
    out : bool
        True if expr+1 is divisible by 2, False otherwise.

    Examples
    --------
    >>> xt.odd_q(1)
    True    

    >>> xt.odd_q(2)
    False
    
    >>> # a departure from wolfram, odd_q works for floats 
    >>> xt.odd_q(1.0)
    True
    
    >>> # odd_q works for non-integer numbers, returns false
    >>> xt.odd_q(0.4)
    False
    
    >>> # it also works on lists:
    >>> xt.odd_q(range(5))
    [False, True, False, True, False]
    """
    try:
        iter(expr)
    except:
        return expr%2==1
    else:
        return [odd_q(i) for i in expr]

