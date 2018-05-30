import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        lock.acquire()
        balance.value = balance.value + 1 # note that this is the crtical part that locks required.
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

def main():
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()

    dep = multiprocessing.Process(target = deposit, args = (balance,lock))
    wdt = multiprocessing.Process(target = withdraw, args = (balance,lock))

    dep.start()
    wdt.start()

    dep.join()
    wdt.join()

    print(balance.value)

if __name__ == '__main__':
    main()
