#import matrix plot library
import matplotlib.pyplot as plt

# import the matrix class
from PlayLA.matrix import Matrix

# import the vector class
from PlayLA.vector import Vector

import math

if __name__ == "__main__":
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]
    
    #get the x, y values from the points
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    
    #optimize the size of the canvas
    plt.figure(figsize=(5, 5))

    #set the x, y limits of the canvas
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    #import the arguments of the shape
    plt.plot(x, y)
    
    #create a matrix from the points
    P = Matrix(points)
    
    #get the transformation matrix
    #this matrix is a scaling matrix
    T = Matrix([[2, 0], [0, 1.5]])

    #this matrix is a flip matrix,flip according to the y axis
    T2 = Matrix([[-1, 0], [0, 1]])

    #this matrix is a flip matrix,flip according to the x axis
    T3 = Matrix([[1, 0], [0, -1]])

    #this is a flip matrix,flip according to the origin
    T4 = Matrix([[-1, 0], [0, -1]])

    #shear matrix one
    T5 = Matrix([[1, 1], [0, 1]])

    #shear matrix two
    T6 = Matrix([[1, 0], [1, 1]])

    #create a rotation matrix
    theta = math.pi / 3
    T7 = Matrix([[math.cos(theta), math.sin(theta)],
                 [-math.sin(theta), math.cos(theta)]])
    
    #transform the matrix

    #transform the matrix
    #and first transpose P cos P is a 10*2 matrix
    P2 = T6.dot(P.T())
    
    #plot the transformed points
    # this matrix has been transposed
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
             [P2.col_vector(i)[1] for i in range(P2.col_num())])
    
    #create a flipping book
    T8 = Matrix([[1, 0], [2, 1]])
    #transform the matrix
    P3 = T8.dot(P.T())
    #plot the transformed points
    plt.plot([P3.col_vector(i)[0] for i in range(P3.col_num())],
             [P3.col_vector(i)[1] for i in range(P3.col_num())])
    T9 = Matrix([[1, 0], [3, 1]])
    P4 = T9.dot(P.T())
    plt.plot([P4.col_vector(i)[0] for i in range(P4.col_num())],
             [P4.col_vector(i)[1] for i in range(P4.col_num())])
    #mirror the points above according to the y axis
    plt.plot([-P2.col_vector(i)[0] for i in range(P2.col_num())],
             [P2.col_vector(i)[1] for i in range(P2.col_num())])
    plt.plot([-P3.col_vector(i)[0] for i in range(P3.col_num())],
             [P3.col_vector(i)[1] for i in range(P3.col_num())])
    plt.plot([-P4.col_vector(i)[0] for i in range(P4.col_num())],  
             [P4.col_vector(i)[1] for i in range(P4.col_num())])
    
    x = [-i for i in x]  # 先取反所有元素
    plt.plot(x, y)       # 然后绘制

        
    #run the pyplot window
    plt.show()
    