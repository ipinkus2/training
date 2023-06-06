def joke():
    '''
    This is called a docstring. It explains
    exactly what the function does.
    '''
    return ('Getting a PhD is simple')


def add(a, b):
    '''
    Add two variables together

    Parameters
    ----------
    a : float
        First number to add
    b : float
        Second number to add
    
    Returns
    -------
    c : float
        Sum of a and b
    '''
    # TODO: generalize so we can add more than floats
    c = a - b   # oops, fix this mistake
    return c


def needs_formatting(a,b,c,d):
    ''' Doc strings can be one line too '''
    f = a-b       # comments start at specific points
    g = c*d    # and they will align with each other

    # Note what happens to complex equations
    # Also training whitespace is removed
    answer = (a+b)*(c+d)     
    return answer
