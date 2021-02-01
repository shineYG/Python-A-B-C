# 导入paddlehub库
import paddlehub as hub
import cv2

# 指定模型名称、待预测的图片路径、输出结果的路径，执行并输出预测结果
module = hub.Module(name="deeplabv3p_xception65_humanseg")
res = module.segmentation(paths = ["./beati.jpg"], visualization=True)


# # 指定模型名称、待分词的文本，执行并输出预测结果
# lac = hub.Module(name="lac")
# test_text = ["1996年，曾经是微软员工的加布·纽维尔和麦克·哈灵顿一同创建了Valve软件公司。他们在1996年下半年从id software取得了雷神之锤引擎的使用许可，用来开发半条命系列。"]
# res = lac.lexical_analysis(texts = test_text)
# # 打印预测结果
# print("中文词法分析结果：", res)



# ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")
# results = ocr.recognize_text(images=[cv2.imread('pics.png')])
# # print(result[0]['data'])
# for result in results:
#     # print(result)
   
#     data = result['data']
#     save_path = result['save_path']
#     for infomation in data:
#         print('text: ', infomation['text'], '\nconfidence: ', infomation['confidence'], '\ntext_box_position: ', infomation['text_box_position'])
#     print('--------------------------------------------------------')
