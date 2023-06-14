import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read file csv wiht panda
df_apps = pd.read_csv("googleplaystore.csv")

# initailize the all columns
df_apps = df_apps.drop(columns = ["App", "Category", "Rating", "Reviews", "Size", "Installs", "Type", "Price", "Content Rating", "Genres", "Last Updated", "Current Ver", "Android Ver"])

# filter apps free
df_apps_free = df_apps[df_apps["Price"] == "Free"]

# filter apps paid
df_apps_paid = df_apps[df_apps["Price"] == "Paid"]

# calcul the median rating's apps free
print(df_apps_free["Rating"].median())

# calcul the median rating's apps pay
print(df_apps_paid["Rating"].median())

# display the result in a graph
plt.bar(df_apps_free["Rating"].median(), df_apps_paid["Rating"].median())



