import math
from ._global import is_zero

class Vector:

    def __init__(self, lst):

        """
        Initialize the vector with a list of values.
            
        Args:
        lst: List of numerical values to initialize the vector.
        """
        self._values = list(lst)

    #Enter the values and generate a copy of the vector 
    def underlying(self):
        return self._values[:]

    def __add__(self, another):
        """Adds another vector to this vector element-wise.
            
        Args:
                another (Vector): The vector to add to this vector.
                
        Returns:
                Vector: A new vector resulting from the element-wise addition.
                
        Raises:
                AssertionError: If the vectors have different lengths.
        """
        assert len(self) == len(another), \
            "Error in adding. Lengths of vectors must be the same."
        return Vector([x + y for x, y in zip(self, another)])
    
    def __sub__(self, another):
        assert len(self) == len(another), \
            "Error in subtracting. Lengths of vectors must be the same."
        return Vector([x - y for x, y in zip(self, another)])
    
    def dot(self, other):
        assert len(self) == len(other), \
            "Error in dot product. Lengths of vectors must be the same."
        return sum(x * y for x, y in zip(self, other))
    
    def __mul__(self, scalar): 
        """
            Multiply this vector by a scalar.
            
            Args:
                scalar: The scalar value to multiply with each component of the vector.
                
            Returns:
                Vector: A new vector with each component multiplied by the scalar.
        """
        return Vector([x * scalar for x in self])
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        return Vector([x / scalar for x in self])
    
    def __pos__(self):
        return 1 * self
    
    def __neg__(self):
        return -1 * self
    
    #zero vector
    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)
    
    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self))
    
    def normalize(self):
        if is_zero(self.norm()):
            raise ZeroDivisionError('Cannot normalize the zero vector.')
        return Vector(self._values) / self.norm()
    
    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        """Returns the string representation of the vector in the format 'Vector(values)'."""
        return 'Vector({})'.format(self._values)
    
    def __str__(self):
        return '({})'.format(', '.join(str(x) for x in self._values))
          