
def get_primes(n):
    prime_list = []
    n = 1000000
    # n = 100

    for i in range(n):
        if i == 0 or i == 1:
            continue

        is_decided = False
        for prime in prime_list:
            if i % prime == 0:
                is_decided = True
                break

            if prime * prime > i:
                prime_list.append(i)
                is_decided = True
                break

        if not is_decided:
            prime_list.append(i)

    return prime_list


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    n = 1000000
    prime_list = get_primes(n)
    print(datetime.now() - start)
    print(len(prime_list))