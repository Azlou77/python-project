# import panda
import pandas as pd


# initialise  name, weight et height
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
weight = [200, 20, 10, 50, 1000, 2]
height = [2, 1, 0.5, 1.5, 10, 0.3]

# filter animals wich  weight and height are inferior to 100
animals = [animals[i] for i in range(len(animals)) if weight[i] < 100 and height[i] < 1]