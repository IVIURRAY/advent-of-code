with open('./input-data.txt', 'r') as f:
    data = [int(line.replace("\n", '')) for line in f.readlines()]

i = 1
counter = 0

while i < len(data):
    if data[i] > data[i - 1]:
        counter += 1
    i += 1

print(counter)