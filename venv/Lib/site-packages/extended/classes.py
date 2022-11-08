class up_to(int):
    pass


class sow_reap():
    """
    stores a variable for calling up later. .sow(expr) holds expr until .reap() 
    is called, then it releases it. Instantiate a sow_reap and then look at 
    sow and reap individually for more details.

    
    note this is not quite the same functionality as sow and reap in other languages.
    
    Examples
    --------
    
    >>> #You can sow a value to yourself repeatedly:
    >>> a = xt.sow_reap()
    >>> a.sow(0); [a.sow(a.reap()[1][0]+2) for i in range(10)]; a.reap()[1][0]
    20

    >>> #You can turn a nest into a nest_list by sowing each iteration:
    >>> a.reap(lambda: xt.nest_while(lambda x: a.sow(x//2 if x%2==0 else 3*x+1),
    >>>        17,lambda x:x!=1))
    [1, [52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]]
    
    >>> #Same as above, but just return the numbers resulting from 3x+1 calculation:
    >>> a.reap(lambda: xt.nest_while(lambda x: a.sow(x//2 if x%2==0 else 3*x+1, tag = x%2),
    >>>        17,lambda x:x!=1),tag=1)[1]
    [52, 40, 16]
    
    """
    
    def __init__(self):
        self.expr = []

    def sow(self, expr, tag=None):
        """
        stores an item to be released later

        Parameter + Return
        ------------------
        expr : any
            item to be stored.
        tag : tag to specify which items to return

        Examples
        -------
        see xt.sow_reap() for examples
        
        """
        self.expr.append([expr, tag])
        return expr
        
    def reap(self, f=None, tag=None):
        """
        

        Parameters
        ----------
        f : callable, optional
            function to evaluate. Not necessary, you can call this on your own later.
        tag : any, optional
            tag to narrow down. The default is to grab all items.

        Returns
        -------
        list
            list of sown items.  Note that removing a single tag pops all items

        Examples
        --------
        see xt.sow_reap() for examples
        """
        return_val = f()
        if tag is None:
            expr, self.expr = [[i[0] for i in self.expr], []]        
        else:
            expr, self.expr = [[i[0] for i in self.expr if i[1]==tag], []]        
        return [return_val, expr]


