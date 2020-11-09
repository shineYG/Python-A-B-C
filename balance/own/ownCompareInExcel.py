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
    monthSumInDB = dict()
    yearSumInDB = dict()
    years = set()
    startTime = time.time()

    wb = openpyxl.load_workbook('own.xlsx')
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
        

        monthSumInExcel[month] = round(monthFee, 2)
        year = month[0:4]
        years.add(year)
        yearSumInExcel.setdefault(year, 0)
        yearSumInExcel[year] = round(yearSumInExcel[year] + monthFee, 2)

    print("{}，旧系统欠费汇总完成。。。".format(datetime.datetime.now()))

    # 加载新系统欠费sql语句
    sql = ""
    # with open("own-iwms71.txt", "r", encoding="utf-8") as f: 
    with open("sql-own.txt", "r", encoding="utf-8") as f:  
        sql = f.read()
    
    years = ('2003', '2004')
    #查询新系统，按年、月汇总水费
    for y in sorted(years):
        param = (y+"01", y+"12", y, y, y, y)
        queryResult = queryDB(user71, pw71, dsn71, sql, param)
        yearSumInDB.setdefault(y, 0)
        for res in queryResult:
            # if res[2] in monthSumInDB:
            #     monthSumInDB[res[2]] = round(monthSumInDB[res[2]] + res[1], 2)
            # else:
            #     monthSumInDB[res[2]] = round(res[1], 2)
            yearSumInDB[y] = round(yearSumInDB[y] + res[1], 2) 
        print("{}，新系统{}年欠费汇总完成。。。".format(datetime.datetime.now(), y))
         

    diffFee = list()
    # 比较新旧系统欠费差异
    for y in yearSumInDB:
        if (yearSumInExcel[y] - yearSumInDB[y]) != 0:
            # diffFee.append(("{}，{}年新旧系统欠费数据差异如下。。。".format(datetime.datetime.now(),y),))
            print("{}，{}年数据差异如下：".format(datetime.datetime.now(), y))
            diffFee.append((y, str(yearSumInExcel[y]), str(yearSumInDB[y]), str(yearSumInExcel[y]-yearSumInDB[y])))

            # monthByYear = {k:v for k,v in monthSumInExcel.items() if y in k}
            # for mby in monthByYear:
            #     ym = mby[0:4] + mby[5:]
            #     if monthByYear[mby] - monthSumInDB[ym] != 0:
            #         # diffFee.append(('O', mby, str(monthByYear[mby]), 'N', ym, str(monthSumInDB[ym])))   
            #         diffFee.append(('O', ym, str(monthByYear[mby])))  
            #         diffFee.append(('N', ym, str(monthSumInDB[ym])))   
        else:
            # diffFee.append(("{}，{}年新旧系统欠费一致。。。".format(datetime.datetime.now(), y),))
            print("{}，{}年新旧系统欠费一致。。。".format(datetime.datetime.now(),y))
    # with open("ownFee-log.txt", "w", encoding="utf-8") as l: 
    #     for line in diffFee:
    #         l.write(' '.join(line))
    #         l.write('\r')
    wbDiff = openpyxl.Workbook()
    wsDiff = wbDiff.active
    wsDiff.append(['年份', '旧值', '新值', '差值'])
    for d in diffFee:
        wsDiff.append([d[0], d[1], d[2], d[3]])
    wbDiff.save("diffOwn.xlsx")


    # diffFee.append(("{}，耗时{}秒，完成新旧系统欠费对比。。。".format(datetime.datetime.now(), round((time.time() - startTime),2)),))
    print("{}，耗时{}秒，完成新旧系统欠费对比。。。".format(datetime.datetime.now(), round((time.time() - startTime),2)))

except Exception as e:
    print(e)


