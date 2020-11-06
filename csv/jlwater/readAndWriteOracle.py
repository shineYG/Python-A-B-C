import csv
import time
import cx_Oracle

userRead = 'water'
pwRead = 'water'
dsnRead = "192.168.0.72/orcl"


# 控制每批次插入的数量
batch = 5000

connectionRead = cx_Oracle.connect(userRead, pwRead, dsnRead, encoding = "UTF-8", nencoding = "UTF-8")
cursorRead = connectionRead.cursor()
readSql = '''
    SELECT RLID,
       RLSMFID,
       RLMONTH,
       RLDATE,
       RLCID,
       RLMID,
       RLMSMFID,
       RLCSMFID,
       RLCCODE,
       RLCHARGEPER,
       RLCPID,
       RLCCLASS,
       RLCFLAG,
       RLUSENUM,
       RLCNAME,
       RLCADR,
       RLMADR,
       RLCSTATUS,
       RLMTEL,
       RLTEL,
       RLBANKID,
       RLTSBANKID,
       RLACCOUNTNO,
       RLACCOUNTNAME,
       RLIFTAX,
       RLTAXNO,
       RLIFINV,
       RLMCODE,
       RLMPID,
       RLMCLASS,
       RLMFLAG,
       RLMSFID,
       RLDAY,
       RLBFID,
       RLPRDATE,
       RLRDATE,
       RLZNDATE,
       RLCALIBER,
       RLRTID,
       RLMSTATUS,
       RLMTYPE,
       RLMNO,
       RLSCODE,
       RLECODE,
       RLREADSL,
       RLINVMEMO,
       RLENTRUSTBATCH,
       RLENTRUSTSEQNO,
       RLOUTFLAG,
       RLTRANS,
       RLCD,
       RLYSCHARGETYPE,
       RLSL,
       RLJE,
       RLADDSL,
       RLSCRRLID,
       RLSCRRLTRANS,
       RLSCRRLMONTH,
       RLPAIDJE,
       RLPAIDFLAG,
       RLPAIDPER,
       RLPAIDDATE,
       RLMRID,
       RLMEMO,
       RLZNJ,
       RLLB,
       RLCNAME2,
       RLPFID,
       RLDATETIME,
       RLSCRRLDATE,
       RLPRIMCODE,
       RLPRIFLAG,
       RLRPER,
       RLSAFID,
       RLSCODECHAR,
       RLECODECHAR,
       RLYEARSL,
       RLYEARDATE FROM RECLIST R WHERE R.RLMONTH = :1
'''

userWrite = 'iwms'
pwWrite = 'iwms'
dsnWrite = "127.0.0.1/orcl"
connectionWrite = cx_Oracle.connect(userWrite, pwWrite, dsnWrite, encoding = "UTF-8", nencoding = "UTF-8")
cursorWrite = connectionWrite.cursor()
writeSql = '''
INSERT INTO RECLIST(RLID,
       RLSMFID,
       RLMONTH,
       RLDATE,
       RLCID,
       RLMID,
       RLMSMFID,
       RLCSMFID,
       RLCCODE,
       RLCHARGEPER,
       RLCPID,
       RLCCLASS,
       RLCFLAG,
       RLUSENUM,
       RLCNAME,
       RLCADR,
       RLMADR,
       RLCSTATUS,
       RLMTEL,
       RLTEL,
       RLBANKID,
       RLTSBANKID,
       RLACCOUNTNO,
       RLACCOUNTNAME,
       RLIFTAX,
       RLTAXNO,
       RLIFINV,
       RLMCODE,
       RLMPID,
       RLMCLASS,
       RLMFLAG,
       RLMSFID,
       RLDAY,
       RLBFID,
       RLPRDATE,
       RLRDATE,
       RLZNDATE,
       RLCALIBER,
       RLRTID,
       RLMSTATUS,
       RLMTYPE,
       RLMNO,
       RLSCODE,
       RLECODE,
       RLREADSL,
       RLINVMEMO,
       RLENTRUSTBATCH,
       RLENTRUSTSEQNO,
       RLOUTFLAG,
       RLTRANS,
       RLCD,
       RLYSCHARGETYPE,
       RLSL,
       RLJE,
       RLADDSL,
       RLSCRRLID,
       RLSCRRLTRANS,
       RLSCRRLMONTH,
       RLPAIDJE,
       RLPAIDFLAG,
       RLPAIDPER,
       RLPAIDDATE,
       RLMRID,
       RLMEMO,
       RLZNJ,
       RLLB,
       RLCNAME2,
       RLPFID,
       RLDATETIME,
       RLSCRRLDATE,
       RLPRIMCODE,
       RLPRIFLAG,
       RLRPER,
       RLSAFID,
       RLSCODECHAR,
       RLECODECHAR,
       RLYEARSL,
       RLYEARDATE) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, 
:11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21, :22, :23, :24, :25, :26, :27, :28,
:29, :30, :31, :32, :33, :34, :35, :36, :37, :38, :39, :40, :41, :42, :43, :44, :45, :46,
:47, :48, :49, :50, :51, :52, :53, :54, :55, :56, :57, :58, :59, :60, :61, :62, :63, :64,
:65, :66, :67, :68, :69, :70, :71, :72, :73, :74, :75, :76, :77, :78)
'''

dataset = list()
try:
    inputFile = open('ym.csv', encoding='utf-8')
    fileReader = csv.reader(inputFile)
    for row in fileReader:
        start = time.time()
        cursorRead.execute(readSql, (row[0],))
        readDatas = cursorRead.fetchall()
        queryTime = time.time()
        print('从Oracle查询{}月数据， 耗时 {} 秒'.format(row[0], round((queryTime - start),2)))
        for index,readData in enumerate(readDatas):
            # print(index, len(readDatas), type(readData))
            dataset.append(readData)
            if len(dataset) % batch == 0: 
                cursorWrite.executemany(writeSql, dataset)
                connectionWrite.commit()
                dataset.clear()
                continue
            if index+1 == len(readDatas):
                cursorWrite.executemany(writeSql, dataset)
                connectionWrite.commit()
                dataset.clear()
        print('向Oracle插入{}月数据， 耗时 {} 秒'.format(row[0], round((time.time() - queryTime),2)))
except Exception as e:
    print(e)
finally:
    cursorWrite.executemany(writeSql, dataset)
    connectionWrite.commit()
    dataset.clear()
    cursorRead.close()
    connectionRead.close()
    cursorWrite.close()
    connectionWrite.close()
    inputFile.close()




