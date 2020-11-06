import time
start_time = time.time()

# @timeit
def prime_factors(n):#This computes the list of prime factors of n. I took it from https://codereview.stackexchange.com/questions/121862/fast-number-factorization-in-python and modified it (as advised) to make it faster.
    prime_factor_list = []
    while not n % 2:
        prime_factor_list.append(2)
        n //= 2
    while not n % 3:
        prime_factor_list.append(3)
        n //= 3
    i = 5
    while n != 1:
        while not n % i:
            prime_factor_list.append(i)
            n //= i
        i += 2

    return prime_factor_list

max = 225000#Make this big enough.
sol=0
for k in range(2,max,1):
    if len(set(prime_factors(k)))>3:
        if len(set(prime_factors(k+1))) > 3:
            if len(set(prime_factors(k + 2))) > 3:
                if len(set(prime_factors(k + 3))) > 3:
                    sol = k
                    k = max

if sol>0:
    print(sol,prime_factors(sol),sol+1,prime_factors(sol+1),sol+2,prime_factors(sol+2),sol+3,prime_factors(sol+3))


print("--- %s seconds ---" % (time.time() - start_time))

#The solution is 134043. It took 562.9127 seconds to find. This is lucky, I had estimated that reaching 225000 would take about 10 minutes. I could not have gone much higher.
