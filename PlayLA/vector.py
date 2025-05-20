import math

class Vector:

    def __init__(self, lst):

        """
        Initialize the vector with a list of values.
            
        Args:
        lst: List of numerical values to initialize the vector.
        """
        self._values = list(lst)

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
    
    def __mul__(self, scalar): 
        return Vector([x * scalar for x in self])
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
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
          