from PlayLA.matrix import Matrix

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