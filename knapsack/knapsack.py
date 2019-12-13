#!/usr/bin/python

import sys
from collections import namedtuple


Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  #python sets the default recursion limit at 999
  #the large dataset requires a depth of around 1020
  #an iterative solution is required to solve the large dataset
  sys.setrecursionlimit(1111)
  
  #create a hash table
  brownies = dict()

  def farts(count, cap, rec=0):
    #base result
    value = 0
    chosen = []

    #check if this has been done before
    #if not declare a new definition for the dictionary
    if count in brownies:
      if cap in brownies[count]:
        return brownies[count][cap]
    else:
      brownies[count] = dict()

    #base cases
    #no more items to check, no more space to fill
    if count == 0 or capacity == 0: value = 0

    #if item is too big, move on to the next one
    elif items[count-1].size > cap:
      # value, chosen = farts(count-1, cap)['Value'], farts(count-1, cap)['Chosen']
      tmp = farts(count-1, cap)
      value = tmp['Value']
      chosen = tmp['Chosen']
    
    #decide if we should take the item
    else:
      take = farts(count-1, cap-items[count-1].size)
      donttake = farts(count-1, cap)
      if items[count-1].value + take['Value'] > donttake['Value']:
        value = items[count-1].value + take['Value']
        chosen = take['Chosen'] + [count]
      else:
        value = donttake['Value']
        chosen = donttake['Chosen']
    
    brownies[count][cap] = {'Value': value, 'Chosen': chosen}
    return {'Value': value, 'Chosen': chosen}
  return farts(len(items), capacity)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')