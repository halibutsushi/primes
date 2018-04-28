import multiprocessing as mp
import pyprimes

class Worker:

    def __init__(self, start_num, stop_num, out_q):
        self.out_q = out_q
        self.proc = mp.Process(target=self._is_prime, args=(start_num, stop_num))
        self.cache = []

    def _is_prime(self, start_num, stop_num):
        for i in range(start_num, stop_num):
            self.cache.append((i, pyprimes.isprime(i)))

        self.out_q.put(self.cache)

    def start(self):
        self.proc.start()

    def stop(self):
        self.proc.join()

if __name__ == "__main__":
    out_q = mp.SimpleQueue()
    workers = []

    n = 1000000
    n = 1000
    interval = n // 4
    if n % 4 > 0:
        interval += 1

    for i in range(0, n, interval):
        end = min(i + interval, n)
        workers.append(Worker(i, end, out_q))

    for w in workers:
        w.start()

    for w in workers:
        w.stop()

    results = []
    for _ in range(4):
        results += out_q.get()

    print(results)