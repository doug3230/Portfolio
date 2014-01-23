"""
-------------------------------------------------------
[class file name]
[description of classes]
-------------------------------------------------------
Author:  Richard Douglas
Email:   doug3230@mylaurier.ca
Version: 2014-01-21
-------------------------------------------------------
"""
import rational_functions

#[constants]

class Rational:
    """
    -------------------------------------------------------
    [class description]
    -------------------------------------------------------
    public variables:
        [variable name - description of variable]
    public methods:
        [method name - description of method] 
    -------------------------------------------------------
    """
    
    def __init__(self, num, den = 1):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        assert den != 0, "denominator cannot be 0"
        num, den = rational_functions.normalize(num, den)
        self._num = int(num)
        self._den = int(den)
        return
    
    def __str__(self):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        if self.is_int():
            return str(self._num)
        else:
            return "{0:d} / {1:d}".format(self._num, self._den)
          
    def num(self):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        return self._num 
    
    def den(self):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """ 
        return self._den
    
    def __add__(self, other):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        new_num = (self._num * other._den) + (self._den * other._num)
        new_den = (self._num * other._den)
        return Rational(new_num, new_den)
    
    def __sub__(self, other):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        new_num = (self._num * other._den) - (self._den * other._num)
        new_den = (self._num * other._den)
        return Rational(new_num, new_den) 
        
    def __mul__(self, other):
        """
        -------------------------------------------------------
           [method description]
        -------------------------------------------------------
        Preconditions:
            [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        new_num = (self._num * other._num)
        new_den = (self._den * other._den)
        return Rational(new_num,  new_den)
    
    def __truediv__(self, other):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        assert other != Rational(0), "cannot divide by 0."
        new_num = (self._num * other._den)
        new_den = (self._den * other._num) 
        return Rational(new_num, new_den)
    
    def __eq__(self, other):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        try: 
            same_num = (self._num == other._num)
            same_den = (self._den == other._den)
            return same_num and same_den
        except AttributeError:
            return self.equals_integer(other)
        
    
    def equals_integer(self, integer):
        if not self.is_int():
            return False
        else:
            return (self._num == integer)
    
    def __lt__(self, other):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        lhs = (self._num * other._den)
        rhs = (other._num * self._den)
        return (lhs < rhs) 
        
    def __le__(self, other):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """ 
        return (self < other or self == other)
    
    def is_zero(self):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        return (self._num == 0)
    
    def is_int(self):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """ 
        return (self._den == 1)  
    
    def to_float(self):
        """
        -------------------------------------------------------
        [method description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """ 
        return (self._num / self._den)
        