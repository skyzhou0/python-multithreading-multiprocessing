# Every process has its own address space (virtual memory).
# Thus program variables are not shared between two process. You need
# to use interprocess communication (IPC) techniques if you
# you want to share data between two processess.
#
import time
import multiprocessing

squareRes = []
def calcSquare(n, res):
    global squareRes

    print("calculate square of a number.")
    for i in n:
        print('sqaure: {}'.format(i*i))
        squareRes.append(i*i)
        res.append(i*i)
    print('within a prcoess: result is {}'. format(squareRes))

    # res = squareRes


# Multiprocessing.
def main():

    arr = [2, 3, 8, 9]

    t0 = time.time()
    manager = multiprocessing.Manager()
    res = manager.list()
    p1 = multiprocessing.Process(target = calcSquare, args = (arr,res))

    p1.start()

    p1.join()

    print('result is {}'. format(squareRes)) # This will be empty as the prcoess is not giving back the variable to the main program.
    print('return result via Manager is {}'. format(res)) # This will be empty as the prcoess is not giving back the variable to the main program.
    print('Done!, the run time is: {}'.format(time.time() - t0))

if __name__ == '__main__':

    main()


# using manager in multiprocessing.
# import multiprocessing
#
# def worker(procnum, return_dict):
#     '''worker function'''
#     print(str(procnum) + ' represent!')
#     return_dict[procnum] = procnum
#
#
# if __name__ == '__main__':
#     manager = multiprocessing.Manager()
#     return_dict = manager.dict()
#     jobs = []
#     for i in range(5):
#         p = multiprocessing.Process(target=worker, args=(i,return_dict))
#         jobs.append(p)
#         p.start()
#
#     for proc in jobs:
#         proc.join()
#     print(return_dict.values())
