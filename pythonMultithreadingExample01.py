# If users if doing computational intensive work that operation doesn't
# wait for I/O, then multiprocessing should be used instead.
# However, if there is an I/O waiting, one can take the utilize the thread
# to perform other tasks while the thread is in Idel or I/O waiting. For example
# the following calcSquare and calcCube functions.

import time
import threading

def calcSquare(n):

    print("calculate square of a number.")
    for i in n:
        time.sleep(0.2)
        print('sqaure: {}'.format(i*i))

def calcCube(n):

    print("calculate cube of a number.")
    for i in n:
        time.sleep(0.2)
        print('sqaure: {}'.format(i*i*i))

arr = [2, 3, 8, 9]

# Sequential.
t0 = time.time()
calcSquare(arr)
calcCube(arr)

print('the run time is: {}'.format(time.time() - t0))

# Multithreading.
t0 = time.time()

thread1 = threading.Thread(target = calcSquare, args=(arr,))
thread2 = threading.Thread(target = calcCube, args=(arr,))

thread1.start()
thread2.start()

thread1.join()  # task completed and join back to the main program.
thread2.join()

print('the run time is: {}'.format(time.time() - t0))
