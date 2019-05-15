import json, csv
import _pickle as pickle

# 1st task
json_comments_data = open('comments.json', 'r')
json_comments_data_parsed = json.loads(str(json_comments_data.read()))

csv_comments_data = open('comments.csv', 'w')
csv_writer = csv.writer(csv_comments_data)

count = 0

for emp in json_comments_data_parsed:

      if count == 0:

             header = emp.keys()

             csv_writer.writerow(header)

             count += 1

      csv_writer.writerow(emp.values())

csv_comments_data.close()

# 2nd task
csv_hw_data = open('hw_25000.csv', 'r')

arr = []
with open ('hw_25000.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for csv_row in csv_reader:
        arr.append(csv_row)

with open('hw_25000.json', "w") as json_file:
    json_file.write(json.dumps(arr, indent=4))

# 3rd task

with open('mlb_players.pkl', 'rb') as fpkl, open('mlb_players.json', 'w') as fjson, open('mlb_players.csv','w') as fcsv:
    data = pickle.load(fpkl)
    csv_writer = csv.writer(fcsv)
    json.dump(data, fjson, ensure_ascii=False, sort_keys=True, indent=4)
    count = 0
    for emp in data:

        if count == 0:
            header = emp.keys()

            csv_writer.writerow(header)

            count += 1

        csv_writer.writerow(emp.values())
