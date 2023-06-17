import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob as glob


# read file csv wiht panda
df_football = pd.read_csv("csv/Players_WC2014.csv")


# Count the number of players per team
print(df_football.groupby("Team").size())


# Determine the 3 players with the most distance traveled
player_distances = df_football.groupby('Name')['Distance Covered'].sum().sort_values
print(player_distances)


# Determine the 10 players with higthest speed
player_speed = df_football.groupby('Name')['Top Speed'].sum().sort_values
print(player_speed)

# In this 10 players with higthest speed, determine the players who has the most distance traveled whihout the ball
player_speed_distance = df_football.groupby('Name')['Distance Covered Not In Possession'].sum().sort_values
print(player_speed_distance)

# Determine the players with highest speed
player_speed = df_football.groupby('Name')['Top Speed'].sum().sort_values

# Sort by name team  the players with highest speed
player_speed_team = df_football.groupby(['Team', 'Name'])['Top Speed'].sum().sort_values
print(player_speed_team)












