file = open("kendrick.txt", "rb").readlines()
len_file = len(file)
test = file[:int(len_file / 10)]
valid = file[int(len_file / 10): 2 * int(len_file / 10)]
train = file[2 * int(len_file / 10):]
with open('data/kendrick/test.txt', 'wb') as fd:
    for item in test:
        fd.write(item)

with open('data/kendrick/valid.txt', 'wb') as fd:
    for item in valid:
        fd.write(item)
with open('data/kendrick/train.txt', 'wb') as fd:
    for item in train:
        fd.write(item)
