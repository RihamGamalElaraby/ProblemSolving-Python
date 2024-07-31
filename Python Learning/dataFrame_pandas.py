import pandas as pd

# Define a dictionary with sample data
data = {
    "name": ["ahmed", "ayman", "mostafa"],  # List of names
    "city": ["cairo", "alx", "matroh"],     # Corresponding list of cities
    "age": [20, 23, 45],                    # Corresponding list of ages
    "pyscore": [90, 75, 80]                 # Corresponding list of scores
}

# Define custom row labels
row_labels = [101, 102, 103]

# Create a DataFrame using the data dictionary and custom row labels
df = pd.DataFrame(data, index=row_labels)
print(df)  # Print the entire DataFrame

# Extract and print the 'name' column
names = df["name"]
print(names)

# Print the row with the label 103
print(df.loc[103])

# Print the third row (index position 2)
print(df.iloc[2])

# Print specific columns ('name', 'city') for rows with labels 103 to 105 (inclusive)
print(df.loc[103:105, ["name", "city"]])

# Sort the DataFrame by the 'age' column in ascending order and print it
print(df.sort_values(by=["age"], ascending=[True]))

######################################################################

# Save the DataFrame to a CSV file (corrected file extension to .csv)
df.to_csv(r'E:\ProblemSolving-Python\Python Learning\data.csv')

# Read the DataFrame back from the CSV file, using the first column as the index
df = pd.read_csv(r'E:\ProblemSolving-Python\Python Learning\data.csv', index_col=0)

# Create filters: one for 'pyscore' greater than 70 and another for 'age' less than 35
filter1 = df["pyscore"] > 70
filter2 = df["age"] < 35

# Apply both filters to the DataFrame and overwrite df with the filtered result
df = df[filter1 & filter2]

# Print the filtered DataFrame
print(df)
