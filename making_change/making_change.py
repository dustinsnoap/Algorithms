#!/usr/bin/python

import sys

def making_change(amount, denominations=None):
  table = [1] * (amount + 1)
  for i in range(len(denominations)-1):
    for j in range(denominations[i+1],amount+1):
      table[j] += table[j-denominations[i+1]]
  return table[-1]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")