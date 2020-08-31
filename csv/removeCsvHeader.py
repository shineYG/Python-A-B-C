import csv
import pathlib
import shutil

srcPath = 'D:\\Project\\vsCode\\Python-A-B-C\\csv\\removeCsvHeader'
destPath = 'D:\\Project\\vsCode\\Python-A-B-C\\csv\\headerRemoved'

withHeaderPath = pathlib.Path(srcPath)
withOutHeaderPath = pathlib.Path(destPath)

if not withOutHeaderPath.exists():
    shutil.copytree(srcPath, destPath)
else:
    for file in [f for f in withHeaderPath.iterdir() if f.is_file]:
        shutil.copy(str(file), destPath)

for csvFilename in withOutHeaderPath.iterdir():
    csvRows = []

    # 读取文件，去除表头
    csvFile = open(csvFilename)    
    csvReader = csv.reader(csvFile) 
    for row in csvReader:
        if csvReader.line_num == 1:
            continue
        csvRows.append(row)
    csvFile.close()

    # 写入文件，Windows系统下记录中间会多出一行空白，使用 newline='' 去除
    csvOutFile = open(csvFilename, 'w', newline='')
    csvWriter = csv.writer(csvOutFile)  
    csvWriter.writerows(csvRows)
    csvOutFile.close()
