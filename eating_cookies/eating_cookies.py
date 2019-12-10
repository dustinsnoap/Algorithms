#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  ns = [1,1,2]
  combos = 0
  if n < 3: combos = ns[n]
  else:
    for _ in range(3, n):
      ns.insert(3,ns[0] + ns[1] + ns[2])
      ns.pop(0)
    for n in ns:
      combos += n
  return combos

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')