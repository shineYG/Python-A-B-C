from pathlib import Path
from PIL import Image

PATH = 'D:\\Project\\vsCode\\Python-A-B-C\\image\\addLogo'

# 重置logo尺寸
def resizeLogo(p):
    logo = Image.open(str(p))
    width, height = logo.size
    nWidth, nHeight = int(width/4), int(height/4)
    logoName = str(p.parent/'withLogo'/'smallLogo.png')
    logo.resize((nWidth, nHeight)).save(logoName)
    return nWidth, nHeight, logoName

mainPath = Path(PATH)
imageWithLogo = mainPath.joinpath('withLogo')
imageWithLogo.mkdir(exist_ok=True)

# 获取新的logo大小，路径
logoWidth, logoHeight, logoPath = resizeLogo(Path(PATH, 'logo.png'))
logoImg = Image.open(logoPath)

# 遍历需要添加logo的图片目录
for image in mainPath.iterdir():
    name = image.name
    # 判断是否是图片，排除logo自身
    if not (name.endswith('.jpg') or name.endswith('.png')) or name == 'logo.png':
        continue
    img = Image.open(str(mainPath.joinpath(name)))
    width, height = img.size
    # 添加logo
    img.paste(logoImg, (width-logoWidth, height-logoHeight), logoImg)
    # 保存新地址
    img.save(str(imageWithLogo.joinpath(name)))

# 删除logo
Path(logoPath).unlink()
