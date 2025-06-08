from .matrix import Matrix
from .vector import Vector
from ._global import is_zero

"""create a class called LinearSystem 
that takes in a list of lists of numbers and has a method called solve 
that returns a list of the solution to the system of equations represented by the input."""
class LinearSystem :
    #A represent the coefficient matrix, b represent the constant matrix
    def __init__(self, A, b):
        assert A.row_num() == len(b), \
            "The number of rows in A must be equal to the number of elements in b."
        self._m = A.row_num()
        self._n = A.col_num()
        #create a pivot list
        self.pivots = []
        #create a argument matrix
        self.Ab = [A.row_vector(i).underlying() + [b[i]] 
                   for i in range(self._m)]

    #create forward elimination method
    #find the index of row contains the max element in the current column
    def _max_row(self, index_i, index_j, n):
        #initialize the max element(self.Ab[index_i][index_j]) and the max row index(index_i)
        best, ret = self.Ab[index_i][index_j], index_i
        for row in range(index_i + 1, n):
            if abs(self.Ab[row][index_j]) > abs(best):
                best, ret = self.Ab[row][index_j], row
        #return the max row index
        return ret

        """do the exchange between rows to make sure that 
        the diagonal element is the largest one in the current column """
    def _forward(self):
        #the location of the current cycle
        i, k = 0, 0
        while i < self._m and k < self._n:
            #judge if Ab[i][k] can be the pivot
            max_row = self._max_row(i, k ,self._m)
            #if the max element is not on the diagonal, exchange the rows
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            #judge if the pivot is 0
            if is_zero(self.Ab[i][k]):
                #to next column
                k += 1
            else:
                #turn the pivot to 1 
                self.Ab[i] = Vector(self.Ab[i]) / self.Ab[i][k] 
                #RTZ the rest of the elements in the current column
                for j in range(i + 1, self._m):
                    self.Ab[j] = Vector(self.Ab[j]) - self.Ab[j][k] * Vector(self.Ab[i])
                    #record the columns of pivots
                self.pivots.append(k)
                    #to next row cos it is a while loop
                i += 1

    def _backward(self):
        #get the number of nonezero rows
        n = len(self.pivots)
        #repeat the following step until we reach the first row
        for i in range(n - 1, -1, -1):
            #get the column of the pivot which is stored in the list named pivots
            k = self.pivots[i]
            #RTZ the rest of the elements in the current column
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
                
    #create Gauss - Jordan Elimination method
    def gauss_jordan_elimination(self):
        #do the forward elimination
        self._forward()
        #do the backward elimination
        self._backward()

        """determine whether the augmented matrix has a solution"""
        #traverse all zero rows
        for i in range(len(self.pivots), self._m):
            #determine if the constant matrix is 0,if 0 it has solutions,otherwise no
            if not is_zero(self.Ab[i][-1]):
                return False
            return True

    def fancy_print(self):
        for i in range(self._m):
            #self._n does not include the constant matrix
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end = " ")
            print("|", self.Ab[i][-1])

        