import time

def calculate_time(func):
    start = time.time()
    func()
    end = time.time()

    print("Total time ", end - start)
