import pandas as pd
import json
import ast

# Define columns that need parsing from string to Python objects
columns_to_parse = [
    'belongs_to_collection',
    'genres',
    'production_companies',
    'production_countries',
    'spoken_languages'
]

def try_parse(val):
    if pd.isna(val) or val == '':
        return None
    try:
        # Try to parse using ast.literal_eval for Python-style dict/list strings
        return ast.literal_eval(val)
    except Exception:
        # If parsing fails, return the original value
        return val

# Read the CSV file
df = pd.read_csv('movies_metadata.csv')

# Select the first 3 rows
df = df.head(25)

# Parse the specified columns
for col in columns_to_parse:
    if col in df.columns:
        df[col] = df[col].apply(try_parse)

# Convert DataFrame to a list of dictionaries
records = df.to_dict(orient='records')

# Output as formatted JSON
json_output = json.dumps(records, indent=4, ensure_ascii=False)
print(json_output)

# Optionally, write to a file
with open('product.json', 'w', encoding='utf-8') as f:
    f.write(json_output)
