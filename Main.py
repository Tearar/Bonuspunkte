print("Test")
data_file = open("observation_mix.txt", "r")
for line in data_file:
    print(line.rstrip())
data_file.close()