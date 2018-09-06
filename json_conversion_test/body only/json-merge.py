import json
import glob
import os
import pandas as pd
import csv

filename = "merged_file.json"

#Checks to make sure you aren't duplicating the merged .json file
try:
    os.remove(filename)
except OSError:
    pass

#Merges multiple .json files into one .json file in the same directory
jsonData = []
for f in glob.glob("*.json"):
    with open(f, "r") as infile:
        jsonData.append(json.load(infile))
open(filename, "w")
with open(filename, "w") as outfile:
     json.dump(jsonData, outfile)

#Converts JSON to CSV using pandas
#df = pd.read_json("merged_file.json")
#df.to_csv("merged_file.csv", columns=['people'])


from pandas.io.json import json_normalize
with open('merged_file.json') as data_file:    
     data = json.load(data_file)
df = json_normalize(data, 
                         [['array', '0']], 
                         record_prefix='array.people')
df.to_csv("merged_file.csv")

# from pandas.io.json import json_normalize
# sample_object = {'Name':'John', 'Location':{'City':'Los Angeles','State':'CA'}, 'hobbies':['Music', 'Running']}
# json_normalize(sample_object)
# flat = flatten_json.flatten_json(sample_object)
# json_normalize(flat)
# print(flat)

#x = 'merged_file.json'
#f = csv.writer(open("merged_file_test.csv", "wb+"))
# Write CSV Header, If you dont need that, remove this line
#f.writerow(["people", "pose_keypoints_2d"])
#for x in ('merged_file.json'):
#    f.writerow([x["people"]["pose_keypoints_2d"]])

           
