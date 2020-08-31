from PIL import Image

# 新建图片
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImg.png')

# 新建透明背景图片
im2 = Image.new('RGBA', (20, 20))
im2.save('transparent.png')

# 抠图
ragdoll = Image.open('ragdoll.jpg')
croppedImg = ragdoll.crop((166, 56, 446,300))
croppedImg.save('croppedImg.png')

# 图片复制
ragdollCopy = ragdoll.copy()

# 图片粘贴
ragdollCopy.paste(croppedImg, (0, 0))
ragdollCopy.save('pasted.jpg')

forest = Image.open('forest.jpg')
# 报错： ValueError: bad transparency mask 添加 convert("RGBA")
rabbit = Image.open('rabbit.png').convert("RGBA")
forest.paste(rabbit, (0, 0))
# 透明背景粘贴
forest.paste(rabbit, (400, 400), rabbit)
forest.save('transparentBackground.jpg')

# 制作气球马赛克
hotball = Image.open('hotball.jpg')
cropBalloon = hotball.crop((255, 0, 387, 153))
cropBalloon.save('cropBalloon.jpg')
hotWidth, hotHeight = hotball.size
balloonWidth, balloonHeight = cropBalloon.size
hotballCopy = hotball.copy()

# 遍历大图尺寸，每隔一个小图位置粘贴
for left in range(0, hotWidth, balloonWidth):
    for top in range(0, hotHeight, balloonWidth):
        hotballCopy.paste(cropBalloon, (left, top))
hotballCopy.save('tiled.jpg')


# 缩小图片
ragdoll = Image.open('ragdoll.jpg')
width, height = ragdoll.size
# resize()中参数传元祖， 且数值为int类型，否则报错TypeError: integer argument expected, got float 
halfRagdoll = ragdoll.resize((int(width/2), int(height/2)))
halfRagdoll.save('halfRagdoll.jpg')

# 重置图片尺寸
ragdoll.resize((400, 400)).save('ragdoll400.jpg')

# 旋转图片
ragdoll.rotate(90).save('ragdollRotate90.jpg')
ragdoll.rotate(180).save('ragdollRotate180.jpg')
ragdoll.rotate(270).save('ragdollRotate270.jpg')

ragdoll.rotate(10).save('ragdollRotate10.jpg')
# expand=True 多出显示
ragdoll.rotate(10, expand=True).save('ragdollRotate10_expand.jpg')

# 镜像翻转
forest = Image.open('forest.jpg')
forest.transpose(Image.FLIP_LEFT_RIGHT).save('forestHorizon.jpg')
forest.transpose(Image.FLIP_TOP_BOTTOM).save('forestVertical.jpg')


from PIL import Image

im = Image.new('RGBA', (100, 100))
print('transparent background: {}'.format(im.getpixel((0, 0))))

for x in range(100):
	for y in range(50):
		im.putpixel((x, y), (20, 165, 210))
#
from PIL import ImageColor
#
for x in range(100):
	for y in range(50, 100):
		im.putpixel((x, y), ImageColor.getcolor('violet', 'RGBA'))
#
print('upper part: {}'.format(im.getpixel((0, 0))))
print('lower part: {}'.format(im.getpixel((0, 50))))
#
im.save('putPixel.png')