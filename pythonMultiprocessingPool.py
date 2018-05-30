from multiprocessing import Pool
import multiprocessing as mp
import time

def square(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

def main():
    numProcesses = mp.cpu_count()
    pool = Pool((numProcesses//2))

    t1 = time.time()

    res = pool.map(square, range(10000))

    print(sum(res)/len(res))
    print('run time of excution pool: {}'.format(time.time() - t1))

    # sequential.
    t1 = time.time()
    resSeq = []
    for i in range(10000):
        resSeq.append(square(i))

    print(sum(resSeq)/len(resSeq))
    print('run time of sequential algorithm: {}'.format(time.time() - t1))

if __name__ == '__main__':

    main()
