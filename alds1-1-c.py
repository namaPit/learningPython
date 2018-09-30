import collections


def primes_ordered_dict(n):
    #
    prime_list = []
    non_prime_list = []
    number_dict = collections.OrderedDict(
        ((i, None) for i in range(n + 1)))
    #
    del number_dict[0]
    del number_dict[1]
    while True:
        # get prime
        prime, _ = number_dict.popitem(False)
        prime_list.append(prime)
        # break
        if prime * prime > n:
            break
        # get non primes
        non_prime_list.append(prime * prime)
        for k in number_dict:
            if prime * k <= n:
                non_prime_list.append(prime * k)
            else:
                break
        # delete non primes
        for non_prime in non_prime_list:
            del number_dict[non_prime]
        non_prime_list.clear()

    # add rest of numbers as prime
    prime_list.extend(
        [prime for prime, _ in number_dict.items()])

    return prime_list

n = int(input())
ary = []

for i in range(n):
    ary.append(int(input()))

prm = primes_ordered_dict(max(ary)+1)
# print(prm)

ans = 0

for i in ary:
    if prm.count(i) > 0:
        ans += 1

print(ans)

