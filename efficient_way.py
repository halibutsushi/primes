

if __name__ == "__main__":
    prime_list = []
    results = []
    n = 1000000

    for i in range(n):
        if i == 0 or i == 1:
            results.append((i, False))
            continue

        end_limit = i
        is_decided = False
        for prime in prime_list:
            if i % prime == 0:
                results.append((i, False))
                is_decided = True
                break

            if prime > end_limit:
                results.append((i, True))
                prime_list.append(i)
                is_decided = True
                break

            end_limit = i // prime + 1

        if not is_decided:
            results.append((i, True))
            prime_list.append(i)

    print(results[-100:])
    print(len(prime_list))