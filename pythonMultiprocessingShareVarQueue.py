import multiprocessing

def calcSquare(numbers, q1):
    for n in numbers:
        q1.put(n*n)

def calcCube(numbers, q2):
    for n in numbers:
        q2.put(n*n*n)

def main():

    numbers = [2, 3, 5]
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target = calcSquare, args = (numbers, q1))
    p2 = multiprocessing.Process(target = calcCube, args = (numbers, q2))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    while q1.empty() is not True:
        print(q1.get())

    while q2.empty() is not True:
        print(q2.get())


if __name__ == '__main__':
    main()

# The End.
