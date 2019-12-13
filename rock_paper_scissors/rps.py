#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  count = [0]*n
  result = [['rock']*n]
  carry = False
  while True:
    temp = [0]*n
    if carry == False and count == [2]*n: break
    else: carry = True
    for i in range(n-1, -1, -1):
      if carry:
        if count[i] < 2:
          count[i] += 1
          carry = False
        else:
          count[i] = 0
          carry = True
      if count[i] == 0: temp[i] = 'rock'
      if count[i] == 1: temp[i] = 'paper'
      if count[i] == 2: temp[i] = 'scissors'
    result.append(temp)
  return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')