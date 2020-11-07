import json
import csv

# Example of how to write CSV files and convert them to JSON (and vice-versa). 

wards = {}
with open("wards.json", "r") as jsonout: 
    wards = json.load(jsonout)

header=["name","muni","ward_id","normalized_name","warning","election_day_registered","ballots_cast","nov_1_registered"]
    
with open("wards.csv", "w+", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    for (k, v) in wards.items():
        row = wards[k]
        row["normalized_name"] = k
        writer.writerow(row)
        
wards_json = {}
with open("wards.csv", "r") as f: 
    reader = csv.DictReader(f)
    for row in reader:
        ward = {}
        
        # Write the entries for each
        for entry in header:
            # Blank stuff is ok. 
            if row[entry] is None or len(row[entry])==0:
                continue
            ward[entry] = row[entry]
            
        # Write the key (indexed to a normalized version of ward name)
        wards_json[row["normalized_name"]] = ward
        
with open("csv_to_json.json", "w+") as f:
    json.dump(wards_json, f)