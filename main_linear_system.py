from PlayLA.LinearSystem import LinearSystem
from PlayLA.matrix import Matrix
from PlayLA.vector import Vector

if __name__ == "__main__":
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls0 = LinearSystem(A, b)
    ls0.gauss_jordan_elimination()
    ls0.fancy_print()

    print("\n")

    A1 = Matrix([[-5, -12, 0], [8, 12, 12], [2, 3, 3], [3, 7, 2]])
    b1 = Vector([5, -44, -11, 1])
    ls1 = LinearSystem(A1, b1)
    ls1.gauss_jordan_elimination()
    ls1.fancy_print()