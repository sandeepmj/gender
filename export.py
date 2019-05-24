import csv
csv_columns = ['name','gender','probability', 'count']
dict_data = [{'name': 'John', 'gender': 'male', 'probability': 0.99, 'count': 9931}, {'name': 'Jane', 'gender': 'female', 'probability': 0.99, 'count': 1796}, {'name': 'Kristen', 'gender': 'female', 'probability': 1.0, 'count': 1160}, {'name': 'Matt', 'gender': 'male', 'probability': 1.0, 'count': 4915}, {'name': 'Sandeep', 'gender': 'male', 'probability': 0.89, 'count': 272}, {'name': 'Sulekha', 'gender': 'female', 'probability': 1.0, 'count': 1}, {'name': 'Krithi', 'gender': None}, {'name': 'Peter', 'gender': 'male', 'probability': 1.0, 'count': 4373}, {'name': 'Pat', 'gender': 'female', 'probability': 0.6, 'count': 1242}]
csv_file = "gendered.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
