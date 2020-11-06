import cx_Oracle
import openpyxl
import time

user71 = 'iwms'
pw71 = 'iwms'
dsn71 = "192.168.0.71/orcl"
sql71 = '''
    SELECT CONS_NO
  FROM (SELECT /*+ PARALLEL(10)*/
 DEL.CONS_NO, SUM(NVL(DEL.FEE_SUM, 0)) ALL_FEE
  FROM IWMS.ARC_W_WF_CONS_FEE_DETAIL DEL
  JOIN IWMS.ARC_W_WF_CONS_MP_FEE MP
    ON DEL.MP_FEE_ID = MP.MP_FEE_ID
   AND DEL.CALC_ID = MP.CALC_ID
   AND DEL.YM = MP.YM
  JOIN IWMS.ARC_W_WF_CONS_FEE F
    ON DEL.CALC_ID = F.CALC_ID
   AND DEL.YM = F.YM
   AND MP.FEE_ID = F.FEE_ID
   AND F.FEE_STATUS IN ('A', 'H')
 WHERE DEL.YM = '202010'
   AND DEL.ORG_NO = '3240101'
 GROUP BY DEL.CONS_NO
        MINUS (SELECT /*+ PARALLEL(10)*/
               RLMCODE, SUM(DECODE(RLCD, 'DE', 1, -1) * RDJE) AS ALL_FEE
                FROM WATER.RECLIST, WATER.RECDETAIL
               WHERE RLID = RDID
                 AND RLMONTH = '2020.10'
                 AND RDPIID != '09'
                 AND RDJE > 0
               GROUP BY RLMCODE
              UNION ALL
              SELECT /*+ PARALLEL(10)*/
               RLMCODE, SUM(DECODE(RLCD, 'DE', 1, -1) * RDJE) AS ALL_FEE
                FROM TEST_YCZD_RECLIST, TEST_YCZD_RECDETAIL
               WHERE RLID = RDID
                 AND RLMONTH = '2020.10'
                 AND RDPIID != '09'
                 AND RDJE > 0
               GROUP BY RLMCODE)
        ) T
 WHERE T.ALL_FEE != 0
UNION ALL
SELECT CONS_NO
  FROM ((SELECT /*+ PARALLEL(10)*/
          RLMCODE AS CONS_NO, SUM(DECODE(RLCD, 'DE', 1, -1) * RDJE) AS ALL_FEE
           FROM WATER.RECLIST, WATER.RECDETAIL
          WHERE RLID = RDID
            AND RLMONTH = '2020.10'
            AND RDPIID != '09'
            AND RDJE > 0
          GROUP BY RLMCODE
         UNION ALL
         SELECT /*+ PARALLEL(10)*/
          RLMCODE, SUM(DECODE(RLCD, 'DE', 1, -1) * RDJE) AS ALL_FEE
           FROM TEST_YCZD_RECLIST, TEST_YCZD_RECDETAIL
          WHERE RLID = RDID
            AND RLMONTH = '2020.10'
            AND RDPIID != '09'
            AND RDJE > 0
          GROUP BY RLMCODE) MINUS SELECT /*+ PARALLEL(10)*/
 DEL.CONS_NO, SUM(NVL(DEL.FEE_SUM, 0)) ALL_FEE
  FROM IWMS.ARC_W_WF_CONS_FEE_DETAIL DEL
  JOIN IWMS.ARC_W_WF_CONS_MP_FEE MP
    ON DEL.MP_FEE_ID = MP.MP_FEE_ID
   AND DEL.CALC_ID = MP.CALC_ID
   AND DEL.YM = MP.YM
  JOIN IWMS.ARC_W_WF_CONS_FEE F
    ON DEL.CALC_ID = F.CALC_ID
   AND DEL.YM = F.YM
   AND MP.FEE_ID = F.FEE_ID
   AND F.FEE_STATUS IN ('A', 'H')
 WHERE DEL.YM = '202010'
   AND DEL.ORG_NO = '3240101'
 GROUP BY DEL.CONS_NO
       ) T
 WHERE T.ALL_FEE != 0
    '''

# user72 = 'water'
# pw72 = 'water'
# dsn72 = '192.168.0.72/orcl'
# sql72 = '''
# select /*+ parallel(10)*/
#  rlmcode, 
#  sum(decode(rlcd, 'DE', 1, -1) * rdje) as all_fee
#   from reclist, recdetail
#  where rlid = rdid
#  and rlmonth = '2020.10'
#  and rdpiid!='09'
#  and rdje > 0
#  group by rlmcode
# '''

sql = '''
SELECT /*+ PARALLEL(10)*/
 'N' AS R_FLAG, DEL.CONS_NO, SUM(NVL(DEL.FEE_SUM, 0)) ALL_FEE
  FROM IWMS.ARC_W_WF_CONS_FEE_DETAIL DEL
  JOIN IWMS.ARC_W_WF_CONS_MP_FEE MP
    ON DEL.MP_FEE_ID = MP.MP_FEE_ID
   AND DEL.CALC_ID = MP.CALC_ID
   AND DEL.YM = MP.YM
  JOIN IWMS.ARC_W_WF_CONS_FEE F
    ON DEL.CALC_ID = F.CALC_ID
   AND DEL.YM = F.YM
   AND MP.FEE_ID = F.FEE_ID
   AND F.FEE_STATUS IN ('A', 'H')
 WHERE DEL.YM = '202010'
   AND DEL.ORG_NO = '3240101'
   AND DEL.CONS_NO = :1
 GROUP BY DEL.CONS_NO
UNION ALL
SELECT /*+ PARALLEL(10)*/
 'O', RLMCODE, SUM(DECODE(RLCD, 'DE', 1, -1) * RDJE) AS ALL_FEE
  FROM WATER.RECLIST, WATER.RECDETAIL
 WHERE RLID = RDID
   AND RLMONTH = '2020.10'
   AND RDPIID != '09'
   AND RDJE > 0
   AND RLMCODE = :2
 GROUP BY RLMCODE
UNION ALL
SELECT /*+ PARALLEL(10)*/
 'O', RLMCODE, SUM(DECODE(RLCD, 'DE', 1, -1) * RDJE) AS ALL_FEE
  FROM TEST_YCZD_RECLIST, TEST_YCZD_RECDETAIL
 WHERE RLID = RDID
   AND RLMONTH = '2020.10'
   AND RDPIID != '09'
   AND RDJE > 0
   AND RLMCODE = :3
 GROUP BY RLMCODE

'''

def queryCons(user, pw, dsn, sql):
    connection= cx_Oracle.connect(user, pw, dsn, encoding = "UTF-8", nencoding = "UTF-8")
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def queryRcvbl(user, pw, dsn, sql, param):
    connection= cx_Oracle.connect(user, pw, dsn, encoding = "UTF-8", nencoding = "UTF-8")
    cursor = connection.cursor()
    cursor.execute(sql, param)
    return cursor.fetchall()


try:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['新旧标识', '户号', '金额'])

    finalRes = list()
    start = time.time()
    result71 = queryCons(user71, pw71, dsn71, sql71)
    newTime = time.time()
    print('耗时{}秒，新系统应收查询结束。。。'.format(round((newTime - start),2)))

    for x in result71:
        result = queryRcvbl(user71, pw71, dsn71, sql, (x[0], x[0], x[0]))
        for row in result:
            ws.append([row[0], row[1], row[2]])
            print(row)

    # result72 = queryRcvbl(user72, pw72, dsn72, sql72)
    # oldTime = time.time()
    # print('耗时{}秒，旧系统应收查询结束。。。'.format(round((oldTime - newTime),2)))

    # for row71 in result71:  
    #     res72 = [x for x in result72 if x[0] == row71[0]]
    #     if len(res72) == 0:
    #         ws.append([row71[0], row71[1], '', row71[1]])
    #         wb.save('result.xlsx')
    #         continue

    #     print('户号：{}，新值：{}，旧值：{}，差异：{}'.format(row71[0], row71[1], res72[0][1], row71[1]-res72[0][1]))
    #     if row71[1] - res72[0][1] != 0:
    #         ws.append([row71[0], row71[1], res72[0][1], row71[1]-res72[0][1]])
    #         wb.save('result.xlsx')

        # # print(row71)
        # for row72 in result72:
        #     if row71[0] == row72[0]:
        #         ws.append([row71[0], row71[1], row72[1], row71[1]-row72[1]])
        #         result72.remove(row72)   
        #         break
        #         # res = row71[1] - row72[1]
        #         # print('户号：{}, 差值：{}'.format(row71[0], res))
        #         # if res != 0:
        #         #     ws.append([row71[0], row71[1], row72[1], res])
    print('耗时{}秒，新旧系统应收对比结束。。。'.format(round((time.time() - newTime),2)))
    wb.save('result.xlsx')
    
except Exception as e:
    print(e)


