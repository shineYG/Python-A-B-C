import csv
import time
import cx_Oracle

user = 'xxx'
pw = 'xxx'
dsn = "xxx"

# 控制每批次插入的数量
batch = 5000

connection = cx_Oracle.connect(user, pw, dsn, encoding = "UTF-8", nencoding = "UTF-8")

cursor = connection.cursor()

sql = '''
    UPDATE C_WF_CONS C SET C.GA_ADDR = :1 WHERE C.CONS_NO = :2
'''
        
start = time.time()
dataset = list()

try:
    inputFile = open('info.csv', encoding='utf-8')
    fileReader = csv.reader(inputFile)
    for row in fileReader:
        dataset.append((row[4], row[1]))
        if (fileReader.line_num + 1) % batch == 0: 
            cursor.executemany(sql, dataset)
            connection.commit()
            dataset.clear()
            continue
except Exception as e:
    print(e)
finally:
    cursor.executemany(sql, dataset)
    connection.commit()
    dataset.clear()
    cursor.close()
    connection.close()
    inputFile.close()

elapsed = (time.time() - start)


print('向Oracle插入 {} 行，耗时 {} 秒'.format(fileReader.line_num+1, elapsed))



