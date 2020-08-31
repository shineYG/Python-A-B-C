from PIL import ImageColor
from PIL import Image


# 获取颜色的RGB值
print('Red： {}'.format(ImageColor.getcolor('RED', 'RGBA')))

# https://www.rapidtables.com/web/color/RGB_Color.html 颜色获取

ragdoll = Image.open('布偶.jpg')

# 文件的尺寸
print('Size: {}'.format(ragdoll.size))
width, height = ragdoll.size
print('Width: {}\n Height: {}'.format(width, height))

# 文件名
print('Filename: {}'.format(ragdoll.filename))

# 文件格式
print('Format: {}'.format(ragdoll.format))

# 文件描述
print('Description: {}'.format(ragdoll.format_description))

# 文件另存为
ragdoll.save('ragdoll.jpg')
