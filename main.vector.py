from PlayLA.vector import Vector

if __name__ == '__main__':
    #test initialization
    vec = Vector([1, 3])
    print(vec)
    print(len(vec))
    print('vec[0] = {}, vec[1] = {}'.format(vec[0], vec[1]))

    #test addition
    vec2 = Vector([2, 4])
    adding_result = vec + vec2
    print('{} + {} = {}'.format(vec, vec2, adding_result))
    #test subtraction
    print('{} - {} = {}'.format(vec, vec2, vec - vec2))

    #test scalar multiplication
    print('{} * 2 = {}'.format(vec, vec * 2))
    print('2 * {} = {}'.format(vec, 2 * vec))

    #test negation
    print('-{} = {}'.format(vec, -vec))

    #test positive
    print('+{} = {}'.format(vec, +vec))

    #test zero vector
    print('zero vector of dimension 3: {}'.format(Vector.zero(3)))

    #test norm
    print('norm of {} = {}'.format(vec, vec.norm()))

    #test normalization
    print('normalized {} = {}'.format(vec, vec.normalize()))
    print(vec.normalize().norm())
    print(vec2.normalize().norm())

    #test zero vector norm
    try:
        print(Vector.zero(3).normalize())
    except ZeroDivisionError as e:
        print(e)

    #test dot product
    print('dot product of {} and {} = {}'.format(vec, vec2, vec.dot(vec2)))