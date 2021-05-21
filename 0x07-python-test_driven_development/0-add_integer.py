#!/usr/bin/python3
""" add_integer() furncitoin add given integer type and 
retrun the value , check for error [type error] """


def add_integer(a, b=98):
    """ integer addition function  """
    
    """ args if a is not integer and if it is float first must be converted to int
        
        args if b is not integer and if it is float first must be converted to int  """

    if not isinstance(a,(int, float)):
        raise TypeError ("a is a must be an integer")
    elif not isinstance(b,(int, float)):
        raise TypeError ("b is a must be an integer")
    if isinstance(b,float):
        bb = int(b)
    elif isinstance(b,int):
        bb = b
    if isinstance(a,float):
        aa = int(a)
    elif isinstance(a,int):
        aa = a
    return(aa+bb)