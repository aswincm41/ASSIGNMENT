# file handling

#QS1


# file_path = "example.txt"
# with open(file_path, 'w') as file:
#     file.write("Hello, this is some data written to the file.\n")
#     file.write("This is another line in the file.\n")

# print(f"Data has been written to {file_path}")


#QS2


# file_path = "example.txt"

# with open(file_path, 'r') as file:
#     content = file.read()
#     print("Content of the file (read()):")
#     print(content)

# with open(file_path, 'r') as file:
#     print("\nContent of the file (readline()):")
#     line = file.readline()
#     while line:
#         print(line, end="")
#         line = file.readline()


#QS3


# file_path = "example.txt"
# with open(file_path, 'r') as file:
#     content = file.read()
#     print("Content of the file (read()):")
#     print(content)

# with open(file_path, 'r') as file:
#     print("\nContent of the file (readline()):")
#     line = file.readline()
#     while line:
#         print(line, end="")
#         line = file.readline()


#QS4

import csv

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerows(data)
def read_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")
data_to_write = [
    ["John Doe", 25, "New York"],
    ["Jane Smith", 30, "Los Angeles"],
    ["Bob Johnson", 22, "Chicago"]
]


csv_filename = "example.csv"

write_to_csv(csv_filename, data_to_write)
print("Data read from CSV file:")
read_from_csv(csv_filename)


#QS5

######Json####



#QS6

def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

data_to_append = "This is new data to append."

existing_filename = "existing_file.txt"

append_to_file(existing_filename, data_to_append)

with open(existing_filename, 'r') as file:
    file_contents = file.read()
    print("File contents after appending:")
    print(file_contents)
