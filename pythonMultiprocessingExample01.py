# Every process has its own address space (virtual memory).
# Thus program variables are not shared between two process. You need
# to use interprocess communication (IPC) techniques if you
# you want to share data between two processess. 

import time
import multiprocessing

def calcSquare(n):

    print("calculate square of a number.")
    for i in n:
        time.sleep(5)
        print('sqaure: {}'.format(i*i))

def calcCube(n):

    print("calculate cube of a number.")
    for i in n:
        time.sleep(5)
        print('sqaure: {}'.format(i*i*i))

# Multiprocessing.
def main():

    arr = [2, 3, 8, 9]

    t0 = time.time()

    p1 = multiprocessing.Process(target = calcSquare, args = (arr,))
    p2 = multiprocessing.Process(target = calcCube, args = (arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Done!, the run time is: {}'.format(time.time() - t0))

if __name__ == '__main__':

    main()
