import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('data.csv')
print(df.head())
print(df.info())

# Summary Statistics
print(df['Year'].describe())
# Fill NaN values with 0
df['Year'] = df['Year'].fillna(0)

# Convert the Year column to integer
df['Year'] = df['Year'].astype(int)

# PART A: Access Specific Data
# 1. A single row by its label
print(df.loc[df['Year'] == 1999])
# 2. A single row by its position
print(df.iloc[1337])
# 3. A slice of rows by label and another by position
print(df.loc[67:1337])
print(df.iloc[67:1337])
# 4. A single column by name
print(df['Date Of Stop'])
# 5. A single cell by both its row and column labels
print(df.loc[1337, 'Date Of Stop'])

# PART B: Filter a DataFrame Using Boolean Conditions
# 1. Filter that uses a comparison operator
century_20 = df[df['Year'] <= 2000]
print(century_20.head())
# 2. Filter that combines two or more Boolean conditions
no_belt_injury = df[(df["Belts"] == "No") & (df["Personal Injury"] == "Yes")]
print(no_belt_injury.head())

# PART C: Add and Remove Columns
# 1. Create a new column based on an existing column
df["Century"] = np.where(df["Year"] > 2000, "21st", "20th")
# 2. Remove a column
df = df.drop(axis=1, columns=['Geolocation'])
# 3. Print list of remaining columns
print(df.columns)

# PART D: Use groupby() to perform a split-apply-combine operation
color_year = df[df["Year"] > 1888].groupby("Color")["Year"].min()
print("The year of the first car of each color is:")
print(color_year)