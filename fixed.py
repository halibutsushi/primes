import multiprocessing as mp
import pyprimes

class Worker:

    def __init__(self, in_qu, out_q):
        self.q = in_q
        self.proc = mp.Process(target=self._is_prime, args=(out_q,))

    def _is_prime(self, out_q):
        while not self.q.empty():
            elt = self.q.get()
            out_q.put((elt, pyprimes.isprime(elt)))

    def start(self):
        self.proc.start()

    def stop(self):
        self.proc.join()

if __name__ == "__main__":
    in_q = mp.SimpleQueue()
    out_q = mp.SimpleQueue()
    workers = [Worker(in_q, out_q) for _ in range(4)]

    n = 1000000
    for v in range(n):
        in_q.put(v)

    for w in workers:
        w.start()

    for w in workers:
        w.stop()

    results = [out_q.get() for _ in range(n)]

    print(results)