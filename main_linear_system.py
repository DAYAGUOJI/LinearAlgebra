from PlayLA.LinearSystem import LinearSystem
from PlayLA.matrix import Matrix
from PlayLA.vector import Vector

if __name__ == "__main__":
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls0 = LinearSystem(A, b)
    ls0.gauss_jordan_elimination()
    ls0.fancy_print()
    print()

    A1 = Matrix([[-5, -12, 0], [8, 12, 12], [2, 3, 3], [3, 7, 2]])
    b1 = Vector([5, -44, -11, 1])
    ls1 = LinearSystem(A1, b1)
    ls1.gauss_jordan_elimination()
    ls1.fancy_print()
    print()

    A2 = Matrix([[1, -1, 2, 0, 3], [-1, 1, 0, 2, -5], [1, -1, 4, 2, 4], [-2, 2, -5, -1, -3]])
    b2 = Vector([1, 5, 13, -1])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()
    print()

    A3 = Matrix([[2, 2], [2, 1], [1, 2]])
    b3 = Vector([3, 2.5, 7])
    ls3 = LinearSystem(A3, b3)
    if not ls3.gauss_jordan_elimination():
        print("The system has no solution!")
    ls3.fancy_print()
    print()