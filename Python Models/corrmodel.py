import pandas as pd

# Define the data for team1
team1 = {
    'name': ['ahmed', 'mohammed', 'mostafa'],  # List of names
    'age': [28, 29, 30],                       # Corresponding list of ages
    'height': [180, 160, 170],                 # Corresponding list of heights
    'weight': [80, 70, 90]                     # Corresponding list of weights
}

# Create a DataFrame from team1 data
df1 = pd.DataFrame(team1)
print("Team 1 DataFrame:")
print(df1)

# Define the data for team2
team2 = {
    'name': ['reham', 'ola', 'abeer'],         # List of names
    'age': [22, 23, 27],                       # Corresponding list of ages
    'height': [180, 160, 170],                 # Corresponding list of heights
    'weight': [80, 70, 90]                     # Corresponding list of weights
}

# Create a DataFrame from team2 data
df2 = pd.DataFrame(team2)
print("\nTeam 2 DataFrame:")
print(df2)

# Calculate and print the correlation matrix for numerical columns of team1 data
print("\nCorrelation matrix for Team 1 DataFrame:")
print(df1[['age', 'height', 'weight']].corr())

# Calculate and print the correlation matrix for numerical columns of team2 data
print("\nCorrelation matrix for Team 2 DataFrame:")
print(df2[['age', 'height', 'weight']].corr())


# Compute correlation with numerical columns only
correlation = df1[['age', 'height', 'weight']].corrwith(df2[['age', 'height', 'weight']])
print("\nCorrelation between Team 1 and Team 2 DataFrames:")
print(correlation)



