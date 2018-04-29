import multiprocessing as mp
from datetime import datetime


class IdleWorker:
    def __init__(self):
        self.proc = mp.Process(target=self._do_nothing)

    def _do_nothing(self,):
        return None

    def start(self):
        self.proc.start()

    def stop(self):
        self.proc.join()


if __name__ == "__main__":
    start = datetime.now()
    start = datetime.now()
    workers = [IdleWorker() for _ in range(4)]

    for w in workers:
        w.start()

    for w in workers:
        w.stop()

    prime_list = []
    results = []
    n = 1000000
    # n = 100

    for i in range(n):
        if i == 0 or i == 1:
            results.append((i, False))
            continue

        is_decided = False
        for prime in prime_list:
            if i % prime == 0:
                results.append((i, False))
                is_decided = True
                break

            if prime * prime > i:
                results.append((i, True))
                prime_list.append(i)
                is_decided = True
                break

        if not is_decided:
            results.append((i, True))
            prime_list.append(i)

    print(datetime.now() - start)
    print(results[-100:])
    print(len(prime_list))