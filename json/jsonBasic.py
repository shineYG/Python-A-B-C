import json

jsonStr = '{"name":"shine", "age":"30", "gender":"男"}'
# 字符串转json
jsonVal = json.loads(jsonStr)
print(type(jsonVal)) # <class 'dict'>

jsonDict = {"name":"moon", "age":"28", "gender":"女"}
# json转字符串
jsonDisctStr = json.dumps(jsonDict)
print(type(jsonDisctStr)) # <class 'str'>