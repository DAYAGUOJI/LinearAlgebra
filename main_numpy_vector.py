import numpy as np

if __name__ == '__main__':
    vec = np.array([1, 3, 5, 6])
    print(vec)
    print(len(vec))
    print('vec[0] = {}, vec[1] = {}'.format(vec[0], vec[1]))

    print(np.zeros(3))
    print(np.ones(3))
    print(np.full(3, 5))
    print("size = {}".format(vec.size))
    
    vec1 = np.array([1, 2, 3, 4])
    print(vec1[0 :2])
    print(type(vec1[0 :2]))

    #test maths
    print("{} + {} = {}".format(vec, vec1, vec + vec1))
    print("{} - {} = {}".format(vec, vec1, vec - vec1))
    print("{} * 2 = {}".format(vec, vec * 2))
    print("2 * {} = {}".format(vec, 2 * vec))
    print("-{} = {}".format(vec, -vec))
    print("+{} = {}".format(vec, +vec))
    print("zero vector of dimension 3: {}".format(np.zeros(3)))
    print("norm of {} = {}".format(vec, np.linalg.norm(vec)))
    print("normalized {} = {}".format(vec, vec / np.linalg.norm(vec)))