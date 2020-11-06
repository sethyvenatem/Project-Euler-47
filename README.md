# Project-Euler-47

I am starting to learn Python. I have decided to do this by solving problems from the project euler (https://projecteuler.net/) list.

My solution to problem 47 https://projecteuler.net/problem=47

This is a brute force solution, but is gets the job done. The code runs over all the integer numbers k (bigger than 1 and) smaller than max:
- For each k it computes the corresponding list of prime factors.
- Repeated entries in the list are removed by the set() function.
- If the obtained list has more then 4 elements, then the code does the same thing for k+1, and so on until k+3.
- If all four lists (for k, k+1, k+2 and k+3) all have at least 4 elements, then a solution is found and the code stops.

I had to set max = 225000 to find a solution (which is at k = 134043). This is at the boundary of what I can do without being smarter. It took 562.9127 seconds to find. An additional digit would have taken to much time.

I took the prime_factors() function from https://codereview.stackexchange.com/questions/121862/fast-number-factorization-in-python and modified it (as advised) to make it faster.

I could make it faster by changing prime_factors() so that it computes only the first 4 different prime factors. Lists longer than 4 are not nessary.

This time I learned:
- about the len() and set() functions.
- that I should not trust everything that I find online. Indeed, I first used another version of prime_factors() that did not finish the factorisation for all numbers.
