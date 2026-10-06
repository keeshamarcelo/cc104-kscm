import time
from m1simplealgo import sum_iterative, sum_formula

n = 10000000

start = time.time()
sum_iterative(n)
end = time.time()
print("Iterative:", end - start, "seconds")

start = time.time()
sum_formula(n)
end = time.time()
print("Formula:", end - start, "seconds")