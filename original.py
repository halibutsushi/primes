import multiprocessing as mp
import pyprimes

class Worker:
    def _is_prime(self, out_q):
        while True:
            elt = self.q.get()
            if elt == "STOP":
                break
            out_q.put((elt, pyprimes.isprime(elt)))

    def start(self, in_q, out_q):
        self.q = in_q
        self.proc = mp.Process(target=self._is_prime, args=(out_q, ))
        self.proc.start()

    def stop(self):
        self.q.put("STOP")
        self.proc.join()

if __name__ == "__main__":
    in_q = mp.SimpleQueue()
    out_q = mp.SimpleQueue()
    workers = [Worker() for _ in range(4)]

    n = 1000000
    for v in range(n):
        in_q.put(v)

    for w in workers:
        w.start(in_q, out_q)

    for w in workers:
        w.stop()

    results = [out_q.get() for _ in range(n)]