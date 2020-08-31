from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(img)

# 画线
draw.line([(0,0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='pink', width=10)

# 画长方形
draw.rectangle((20, 30, 60, 60), fill='blue')

# 画椭圆形
draw.ellipse((120,30,160,60), fill='red')

# 画多边形
draw.polygon(((80, 82), (70, 75), (100, 120), (140, 55)), fill='yellow', outline='black')

# 循环画线
for i in range(100, 200, 5):
    draw.line([(i, 0), (200, i-100)], fill='pink')

# 写字
draw.text((20, 150), 'Hello', fill='purple')   

# 设置字体样式
SignPainterFont = ImageFont.truetype('C:\\Users\\shine\\AppData\\Local\\Microsoft\\Windows\\Fonts\\signpainterhousescript.ttf', 32)
draw.text((100,150), 'Shine', fill='yellow', font=SignPainterFont)

# 设置中文字体
stFont = ImageFont.truetype("C:\\Windows\\Fonts\\STXINGKA.TTF", 14)
draw.text((160, 180), '木易', fill='black', font=stFont)

img.save('drawing.png')