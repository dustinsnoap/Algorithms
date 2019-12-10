#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  for ingredient in recipe:
    if ingredient in ingredients:
      if ingredients[ingredient] <= 0: batches.append(0)
      else: batches.append(ingredients[ingredient] // recipe[ingredient])
    else: batches.append(0)
  return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))