import json
import glob
import os
import csv


jsonfilename = "merged_file.json"
csvfilename = "merged_file.csv"

try:
    os.remove(jsonfilename)
except OSError:
    pass

try:
    os.remove(csvfilename)
except OSError:
    pass

jsonData = []
for f in glob.glob("*.json"):
    with open(f, "r") as infile:
        jsonData.append(json.load(infile))

with open(jsonfilename, "w") as outfile:
     json.dump(jsonData, outfile)

pose_keypoints = []
people = []
peopleIndex = 0
for data in jsonData:
    for person in data["people"]:
        person_obj = person["pose_keypoints_2d"]
        person_obj.insert(0, ("Person " + str(peopleIndex)))
        people.append(person_obj)
        peopleIndex += 1
    peopleIndex = 0

correctOrientation = list(zip(*people)) #the * wildcard forces zip to treat each sublist in the original list as a separtate argument
print(correctOrientation)
with open(csvfilename, 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for person in correctOrientation:
        wr.writerow(person)

