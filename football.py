import pandas as pd
import numpy as np

# read file csv wiht panda
df_ville = pd.read_csv("C:\xampp\htdocs\python-project\csv\Players_WC2014.csv", delimiter = "\t")

# calcul the median to have the number of players in each teams
print(df_ville["Team"].value_counts())

# create a dictionary with the number of players in each teams
dict_team = dict(df_ville["Team"].value_counts())

