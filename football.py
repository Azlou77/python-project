import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read file csv wiht panda
df = pd.read_csv("csv/Players_WC2014.csv")

# determine the number of players per team
df = pd.read_csv('filename.csv')
team_counts = df.groupby('team_name').size()
print(team_counts)

# determine the 3 players with the most distance traveled
player_distances = df.groupby('Name')['Distance Covered'].sum().sort_values
print(player_distances)
