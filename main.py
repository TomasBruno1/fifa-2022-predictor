import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

matches = pd.read_csv('Datasets/international_matches.csv')

# EDA
print(matches.describe())
print('----------------------------------------')

# Observing total number of rows and columns in the dataset
print(matches.head())
print(matches.tail())
print(matches.shape)  # (23921, 25)
print('----------------------------------------')

# Observing all the columns in the dataset
print(list(matches))
print('----------------------------------------')

# Finding Missing Values
print(matches.isnull().sum())
print('----------------------------------------')

# Drop all rows with missing values
matches = matches.dropna()

print(matches.shape)  # (4303, 25)
print(matches["home_team_continent"])
print(matches["home_team_result"])
print('----------------------------------------')

continent_rows = matches["home_team_continent"]
continent_match_count = continent_rows.value_counts()

# find how many games each continent won
continent_wins = matches[matches["home_team_result"] == "Win"]
continent_wins = continent_wins["home_team_continent"].value_counts()

# plot the number of wins for each continent divided by the number of games played
continent_wins = continent_wins / continent_match_count
sns.barplot(x=continent_wins.index, y=continent_wins.values)
plt.show()

offense = matches.groupby("home_team")["home_team_mean_offense_score"].mean().sort_values(ascending=False)
midfield = matches.groupby("home_team")["home_team_mean_midfield_score"].mean().sort_values(ascending=False)
defense = matches.groupby("home_team")["home_team_mean_defense_score"].mean().sort_values(ascending=False)
goalkeeper = matches.groupby("home_team")["home_team_goalkeeper_score"].mean().sort_values(ascending=False)

# find the mean of all categories
mean = (offense + midfield + defense + goalkeeper) / 4

# make a table with 5 rows and a column for each category
table = pd.DataFrame(index=range(1, 6), columns=["offense", "midfield", "defense", "goalkeeper", "mean"])

# fill the table with the mean values for each category
table["offense"] = offense.values[:5]
table["midfield"] = midfield.values[:5]
table["defense"] = defense.values[:5]
table["goalkeeper"] = goalkeeper.values[:5]
table["mean"] = mean.values[:5]






# replace "Win", "Draw", "Loss" with 1, 0, -1
matches["home_team_result"] = matches["home_team_result"].replace("Win", 1)
matches["home_team_result"] = matches["home_team_result"].replace("Draw", 0)
matches["home_team_result"] = matches["home_team_result"].replace("Loss", -1)

# show dataset
print(matches.head())
