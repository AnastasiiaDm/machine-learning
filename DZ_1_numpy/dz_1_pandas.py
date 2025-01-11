import pandas as pd
import random
import string

data = {
    "Name": ["Geralt", "Ciri", "Lutik", "Yennefer", "Triss"],
    "Age": [57, 21, 45, 90, 50],
    "Weapon": ["Sword", "Sword", None, "Magic", "Magic"]
}
df = pd.DataFrame(data)

df["Random_numbers"] = [random.randint(0, 100) for _ in range(len(df))]
print(df)

filtered_df = df[df['Age'] > 45]
print(f'filtered df: \n{filtered_df}\n')

df = pd.read_csv('wine.csv', nrows=5, header=None)

print(df)

numerical_columns = df.select_dtypes(include=['number'])
general_statistics = numerical_columns.describe()
print(f"General statistics: \n{general_statistics}")

num_columns = df.shape[1]
column_names = list(string.ascii_uppercase[:num_columns])

df.columns = column_names
print(df)

unique_values_column_G = df['G'].unique()
print(f"Unique values in column 'G': {unique_values_column_G}")
