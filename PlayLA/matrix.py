from .vector import Vector

class Matrix:
    
    #create class of zero matrix
    @classmethod
    def zeros(cls, r, c):
        return cls([[0] * c for _ in range(r)])
    @classmethod
    def zero(cls, r, c):
        return cls([[0] * c for _ in range(r)])
    
    #create class of identity matrix
    #return a n * n identity matrix
    @classmethod
    def identity(cls, dim):
        return cls([[1 if i == j else 0 for j in range(dim)] for i in range(dim)])
    
    def T(self):
        """转置矩阵"""
        return Matrix([[e for e in self.col_vector(i)] 
                        for i in range(self.col_num())])

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]
 
    def shape(self):
        return len(self._values), len(self._values[0])
    
    def size(self):
        r, c = self.shape()
        return r * c
    
    def row_num(self):
        return self.shape()[0]
    __len__ = row_num

    def col_num(self):
        return self.shape()[1]
    
    def row_vector(self, i):
        return Vector(self._values[i])
    
    def col_vector(self, j):
        return Vector([row[j] for row in self._values])
    
    def get_row(self, i):
        return Vector(self._values[i])
    
    def get_col(self, j):
        return [row[j] for row in self._values]

    def __getitem__(self, pos):
        """获取矩阵中指定位置的元素"""
        r, c = pos  # 假设pos是一个(row, column)的元组
        return self._values[r][c]
    
    def __add__(self, other):
        assert self.shape() == other.shape(), \
            "Error in adding. Matrix shapes must be the same."
        return Matrix([[x + y for x, y in zip(self_row, other_row)]
                       for self_row, other_row in zip(self._values, other._values)])
    
    def __sub__(self, other):
        assert self.shape() == other.shape(), \
            "Error in subtracting. Matrix shapes must be the same."
        return Matrix([[x - y for x, y in zip(self_row, other_row)]
                       for self_row, other_row in zip(self._values, other._values)])
    
    def dot(self, other):
        if isinstance(other, Vector):
            assert self.col_num() == len(other), \
                "Error in dot product. Vector size must be the same as matrix column number."
            return Vector([self.row_vector(i).dot(other) for i in range(self.row_num())]) 
        elif isinstance(other, Matrix):
            assert self.col_num() == other.row_num(), \
                "Error in dot product. Matrix shapes must be the same."
            return Matrix([self.row_vector(i).dot(other.col_vector(j)) for j in range(other.col_num())]
                          for i in range(self.row_num()))
                           
    
    def __mul__(self, scalar):
        return Matrix([[x * scalar for x in self_row]
                       for self_row in self._values])
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        return self * (1 / scalar)    
    
    def __pos__(self):
        return self * 1
    
    def __neg__(self):
        return self * -1
    
    def __iter__(self):
        return iter(self._values)
    def __repr__(self):
        return "Matrix({})".format(self._values)
    __str__ = __repr__