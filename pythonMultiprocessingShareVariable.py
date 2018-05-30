import multiprocessing
import numpy as np

def calcSquare(n, res, v):

    v.value = np.pi

    print("calculate square of a number.")
    for idx, i in enumerate(n):
        print('sqaure: {}'.format(i*i))
        res[idx] = i * i

    # print('within a prcoess: result is {}'. format(res))

def main():

    arr = [2, 3, 5, 8]

    shareVariable = multiprocessing.Array('i', 4)
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target = calcSquare, args = (arr,shareVariable, v))

    p1.start()
    p1.join()

    print(shareVariable[:])
    print(v.value)

if __name__ == '__main__':
    main()
