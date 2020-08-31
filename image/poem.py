#功能：通过模板图片 写入文字到指定位置，并分别保存成新的图片
#功能说明：根据"\n"换行
#python2与python3共存配置方法https://www.cnblogs.com/thunderLL/p/6643022.html
 
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
 
#初始化字符串
strs = '''李商隐《锦瑟》

锦瑟无端五十弦，一弦一柱思华年。

庄生晓梦迷蝴蝶，望帝春心托杜鹃。

沧海月明珠有泪，蓝田日暖玉生烟。

此情可待成追忆，只是当时已惘然。''' 
#模板图片
imageFile = "forest.jpg"

#初始化参数
x = 30  #横坐标（左右）
y = 20   #纵坐标（上下）
word_size = 50 #文字大小
word_css  = "C:\\Windows\\Fonts\\STXINGKA.TTF" #字体文件   行楷
 
#设置字体，如果没有，也可以不设置
font = ImageFont.truetype(word_css,word_size)
 
#分割得到数组
im1=Image.open(imageFile) #打开图片
draw = ImageDraw.Draw(im1)
draw.text((x, y),strs, 'yellow', font=font) #设置位置坐标 文字 颜色 字体
        
#定义文件名 数字需要用str强转
new_filename = 'forest_poem.jpg'
im1.save(new_filename) 
del draw #删除画笔
im1.close()  #关闭图片