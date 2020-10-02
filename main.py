import logging
import numpy as np

import greeter_lib
import wahoovian

def main():
    # put all code that executes in here
    #  Put your own utlility or helper functions in a separate file that's imported,
#       like greeter_lib.py here.

    logging.basicConfig(filename='hoo-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    logging.info('Program begins!')
    greeter_lib.greeter("Our program begins!")

    isSquare = wahoovian.wahoovian(np.array([[1, 2], [3, 4]]))
    print(isSquare)

    notSquare = np.array([[5, 6, 7], [4, 6]])
    print(wahoovian.wahoovian(notSquare))
    
    logging.info('Program ends!')
    greeter_lib.greeter("Our program ends!")

if __name__ == '__main__':
    main()