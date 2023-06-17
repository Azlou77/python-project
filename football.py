import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read file csv wiht panda
df_football = pd.read_csv("csv/Players_WC2014.csv")


# Count the number of players per team
print(df_football.groupby("Team").size())


# Determine the 3 players with the most distance traveled
player_distances = df_football.groupby('Name')['Distance Covered'].sum().sort_values
print(player_distances)


# Determine the 10 players with higthest speed
player_speed = df_football.groupby('Name')['Sprint Speed'].sum().sort_values
print(player_speed)





