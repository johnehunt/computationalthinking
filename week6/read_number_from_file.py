# Example illustratign reading numeric data from a file

data = None
with open('data.txt', 'r') as f:
    data_as_string = f.readline()
    if data_as_string.isdigit():
        data = int(data_as_string)

print('Data:', data)