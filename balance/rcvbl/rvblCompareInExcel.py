import cx_Oracle
import openpyxl
import time
import datetime

user71 = 'iwms'
pw71 = 'iwms'
dsn71 = "192.168.0.71/orcl"

def queryDB(user, pw, dsn, sql, param):
    connection= cx_Oracle.connect(user, pw, dsn, encoding = "UTF-8", nencoding = "UTF-8")
    cursor = connection.cursor()
    cursor.execute(sql, param)
    return cursor.fetchall()

try:
    monthSumInExcel = dict()
    yearSumInExcel = dict()
    yearSumInDB = dict()
    years = set()
    startTime = time.time()

    wb = openpyxl.load_workbook('rcvbl.xlsx')
    ws = wb.active
    #按年、月汇总水费
    for index, row in enumerate(ws.rows):
        if index == 0:
            continue
        month = row[16].value
        monthFee = (float(row[1].value) + float(row[2].value) + float(row[3].value) 
        + float(row[4].value) + float(row[5].value) + float(row[6].value) + float(row[7].value) + float(row[8].value) + 
        float(row[9].value) + float(row[10].value) + float(row[11].value) + float(row[12].value) + float(row[13].value) + 
        float(row[14].value) + float(row[15].value))
  
        year = month[0:4]
        years.add(year)
        yearSumInExcel.setdefault(year, 0)
        yearSumInExcel[year] = round(yearSumInExcel[year] + monthFee, 2)

    print("{}，旧系统应收汇总完成。。。".format(datetime.datetime.now()))

    # 加载新系统应收sql语句
    sql = ""
    with open("sql-rcvbl.txt", "r", encoding="utf-8") as f:  
        sql = f.read()
    
    years = ('2020', )
    #查询新系统，按年、月汇总水费
    for y in sorted(years):
        param = (y+"01", y+"12")
        result = queryDB(user71, pw71, dsn71, sql, param)
        yearSumInDB[y] = result[0][0]
        print("{}，新系统{}年应收汇总完成。。。".format(datetime.datetime.now(), y))
         

    diffFee = list()
    # 比较新旧系统应收差异
    for y in yearSumInDB:
        if (yearSumInExcel[y] - yearSumInDB[y]) != 0:
            print("{}，{}年数据差异如下：".format(datetime.datetime.now(), y))
            diffFee.append((y, str(yearSumInExcel[y]), str(yearSumInDB[y]), str(yearSumInExcel[y] - yearSumInDB[y])))   
        else:
            print("{}，{}年新旧系统应收一致。。。".format(datetime.datetime.now(),y))

    wbDiff = openpyxl.Workbook()
    wsDiff = wbDiff.active
    wsDiff.append(['年份', '旧值', '新值', '差值'])
    for d in diffFee:
        wsDiff.append([d[0], d[1], d[2], d[3]])
    wbDiff.save("diffRcvbl.xlsx")

    print("{}，耗时{}秒，完成新旧系统应收对比。。。".format(datetime.datetime.now(), round((time.time() - startTime),2)))

except Exception as e:
    print(e)


