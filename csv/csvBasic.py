import csv
import pprint

# 往csv中写数据, Windows系统需要添加 newline=''
file = open('putcsv.csv', 'w', newline='')
fileWriter = csv.writer(file)
fileWriter.writerow(['DATE', 'NAME', 'DESC'])
fileWriter.writerow(['2020-07-01', 'shine', 'test1'])
fileWriter.writerow(['2020-07-02', 'moon', 'test2'])
fileWriter.writerow(['2020-07-03', 'night', 'test3'])
fileWriter.writerow(['2020-07-04', 'sky', 'test4'])
file.close()

# 读取csv中数据
outputFile = open('putcsv.csv')
fileReader = csv.reader(outputFile)
fileList = list(fileReader)
pprint.pprint(fileList)

pprint.pprint('-------------------------------')
outputFile.seek(0)
for row in fileReader:
    print('Row Num # ', fileReader.line_num, row)

outputFile.close()