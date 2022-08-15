import csv
import json

file_words = []
input_file_rows = []
count_dict = []
order_Counts = []
branded_products = []
brand_counts = 0
count = 0
x = 0


def convert_to_json(n):
    return json.loads(str(n))


with open("./input_example.csv", 'r') as file:
    csvReader = csv.reader(file)
    for row in csvReader:
        input_file_rows.append(row)
        for item in row:
            file_words.append(item)

for input_row in input_file_rows:
    orderCount = file_words.count(input_row[2])
    order_Counts.append(json.dumps({"name": input_row[2], "orderCount": orderCount}))
    if len(branded_products) == 0:
        branded_products.append(json.dumps({"name": input_row[2], "brand": input_row[4], "count": brand_counts}))
    else:
        for i in branded_products:
            const = json.loads(str(i))
            if const["brand"] != input_row[4]:
                branded_products.append(json.dumps({"name": input_row[2], "brand": input_row[4], "count": brand_counts}))
            break

branded_products = list(set(branded_products))
order_Counts = list(set(order_Counts))

for order in order_Counts:
    const = json.loads(str(order))
    for i in input_file_rows:
        if i[2] == const["name"]:
            x += 1
            countName = const["name"]
            count += int(i[3])
            if int(const["orderCount"]) == x:
                count_dict.append({"countName": countName, "count": count})
                x = 0
                count = 0
                break

branded_products = list(map(convert_to_json, branded_products))


for ia in branded_products:
    for ro in input_file_rows:
        if ia["brand"] == ro[4]:
            ia["count"] += 1

with open('./0_input_example.csv', 'w', newline='') as file1:
    file1_Writer = csv.writer(file1, delimiter=',')
    for order in count_dict:
        file1_Writer.writerow([order["countName"], int(order["count"]) / len(input_file_rows)])

with open('./1_input_example.csv', 'w', newline='') as file2:
    file2_Writer = csv.writer(file2, delimiter=',')
    for i in branded_products:
        file2_Writer.writerow([i["name"], i["brand"], i["count"]])
