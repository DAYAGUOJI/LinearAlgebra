#import numpy
import numpy as np

if __name__ == "__main__":
    
    #create a numpy matrix
    matrix0 = np.array([[1, 2], [3, 4]])

    #print the matrix
    print(matrix0)

    #print the shape of the matrix
    print(matrix0.shape)

    #print the size of the matrix
    print(matrix0.size)

    #print the element at row 0, column 1
    print(matrix0[0, 1])

    #get the transpose of the matrix
    print(matrix0.T)

    #get the first column of the matrix
    print(matrix0[:, 0])

    #get the first row of the matrix
    print(matrix0[0])

    #create the other matrix
    matrix1 = np.array([[1, 5], [3, 6]])

    #test the operation between two matrices
    print(matrix0 + matrix1)
    print(matrix0 - matrix1)
    print(matrix0 * 2)
    print(np.zeros((2, 3)))
    print(matrix0 * matrix1)
    print(matrix0.dot(matrix1))
