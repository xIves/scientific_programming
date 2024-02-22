"""Module creating a data frame from a dictionary."""

# Import library
import pandas as pd

# Initialize data of lists.
data = pd.DataFrame({'Name': ['tom', 'nick', 'krish', 'jack'],
                     'Age': [20, 21, 19, 18]})

# Create DataFrame
df = pd.DataFrame(data)
print(type(df))

# Print the output
print(df.head())
