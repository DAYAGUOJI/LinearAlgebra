from PlayLA.matrix import Matrix
from PlayLA.vector import Vector

if __name__ == "__main__":
    #test matrix representation
    print(Matrix([[1, 2], [3, 4]]))

    #test matrix shape
    matrix1 = Matrix([[1, 2], [3, 4]])
    print(matrix1.shape())

    #test matrix size
    matrix2 = Matrix([[1, 2], [3, 4]])
    print(matrix2.size())

    #test getitem
    matrix3 = Matrix([[1, 2], [3, 4]])
    print(matrix3[0, 1])

    #test adding
    matrix4 = Matrix([[1, 2], [3, 4]])
    matrix5 = Matrix([[1, 5], [3, 6]])
    print(matrix4 + matrix5)
    print(matrix4 - matrix5)
    print(matrix4 * 2)
    print(Matrix.zero(2, 3))

    matrix6 = Matrix([[2, 1], [3, 5], [4, 6]])
    vector1 = Vector([3, 1])
    print(matrix6.col_num())
    print(matrix6.dot(vector1))

    matrix7 = Matrix([[3, 6], [1, 3]])
    print(matrix6.dot(matrix7))

    #test matrix transpose
    matrix8 = Matrix([[1, 2], [3, 4]])
    print(matrix8.T())
    print(matrix6.T())

    #test generate identity matrix
    I = Matrix.identity(2)
    print(I)
    print("matrix8 * I = {}".format(matrix8.dot(I)))
    print("I * matrix8 = {}".format(I.dot(matrix8)))