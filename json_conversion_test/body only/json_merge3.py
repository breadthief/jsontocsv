import json
import pandas as pd

with open('merged_file.json') as f: # this ensures opening and closing file
    a = json.loads(f.read())

data = a("x")

df = pd.DataFrame(data)

print(df.transpose())
