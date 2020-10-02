import logging
import numpy as np

# The operation takes a square matrix as its input, and returns a square matrix with the same dimensions.
# The output matrix will be the transpose of the input matrix, but with every value in the matrix negated.

# If the input matrix is not square, the function will return the input matrix unchanged.
# If the input matrix has zero rows and columns, the the function will return the input matrix unchanged.

def wahoovian(matrix):
    logging.info('You have entered Wahoovian!')

    rows = len(matrix)
    columns = len(matrix[0])
    # I used this resource: <https://www.kite.com/python/answers/how-to-find-the-dimensions-of-a-matrix-in-python>
    if rows != columns or matrix.size == 0 :
        # input matrix is not a suqare or is empty
        logging.warning('Matrix inputted is not a square!')
        logging.info('You are now leaving Wahoovian!')
        return matrix # return matrix unchanged
    else: 
        # negate and transpose matrix
        # <https://numpy.org/doc/stable/reference/generated/numpy.negative.html>
        logging.info('Input is a square!')
        np.negative(matrix, matrix) # negate and store as new matrix
        matrix.transpose()
        logging.info('You are now leaving Wahoovian!')
        return matrix

