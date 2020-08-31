import csv

empty_num = 0
inputFile = open('info.csv', encoding='utf-8')
fileReader = csv.reader(inputFile)
for row in fileReader:
    if row[4] == '':
        empty_num = empty_num + 1

print('公安地址为空数量: {}'.format(empty_num))

