import multiprocessing as mp
import pyprimes

class Worker:

    def __init__(self, out_q, shared_prime_list):
        self.proc = None
        self.out_q = out_q
        self.prime_list = shared_prime_list

    def _check_divisibility(self, num, start_index, end_index):
        end_limit = num
        is_decided = False
        for prime in self.prime_list[start_index:end_index]:
            if num % prime == 0:
                self.out_q.put(True)
                is_decided = True
                break

            if prime > end_limit:
                self.out_q.put(False)
                is_decided = True
                break

            end_limit = num // prime + 1

        if not is_decided:
            self.out_q.put(False)

    def start(self, num, start_index, end_idex):
        self.proc = mp.Process(target=self._check_divisibility, args=(num, start_index, end_idex))
        self.proc.start()

    def stop(self):
        self.proc.join()

NUM_WORKERS = 4

if __name__ == "__main__":
    results = []
    n = 1000000
    n = 200
    out_q = mp.SimpleQueue()
    # manager = mp.Manager()
    # prime_list = manager.list()
    array_length = mp.Value('i', 0, lock=False)
    prime_array = mp.Array('i', n//2, lock=False)
    workers = [Worker(out_q, prime_array) for _ in range(NUM_WORKERS)]


    for i in range(n):
        if i == 0 or i == 1:
            results.append((i, False))
            continue

        if i == 2:
            results.append((i, True))
            # prime_list.append(i)
            prime_array[0] = i
            array_length.value += 1
            continue

        num_prime_discovered = array_length.value
        interval = num_prime_discovered // NUM_WORKERS
        if num_prime_discovered % NUM_WORKERS > 0:
            interval += 1

        worker_index = 0
        for j in range(0, num_prime_discovered, interval):
            worker = workers[worker_index]
            end_index = min(array_length.value, j + interval)
            worker.start(i, j, end_index)
            worker_index += 1

        divisibility = False
        for j in range(worker_index):
            workers[j].stop()

        for j in range(worker_index):
            divisibility = out_q.get() or divisibility

        if divisibility is False:
            #prime_list.append(i)
            prime_array[array_length.value] = i
            array_length.value += 1
            results.append((i, True))
        else:
            results.append((i, False))

    print(results[-100:])