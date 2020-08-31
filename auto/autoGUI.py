import pyautogui, time, pprint

# ---------------------鼠标在画板上画迷宫-------------------
# time.sleep(3)
# # 点击鼠标，使画板置顶
# pyautogui.click(100, 300)
# distance = 200
# interval = 5

# D = 0.1

# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=D)
#     distance = distance - interval
#     pyautogui.dragRel(0, distance, duration=D)
#     pyautogui.dragRel(-distance, 0, duration=D)
#     distance = distance - interval
#     pyautogui.dragRel(0, -distance, duration=D)

# ---------------------------------------------------------


# Moving the Mouse
# for i in range(10):
#       pyautogui.moveTo(100, 100, duration=0.25)
#       pyautogui.moveTo(200, 100, duration=0.25)
#       pyautogui.moveTo(200, 200, duration=0.25)
#       pyautogui.moveTo(100, 200, duration=0.25)

# for i in range(10):
#       pyautogui.moveTo(100, 100)
#       pyautogui.moveTo(200, 100)
#       pyautogui.moveTo(200, 200)
#       pyautogui.moveTo(100, 200)

# 鼠标相对当前位置移动
# time.sleep(2)
# for i in range(10):
#       pyautogui.moveRel(100, 0, duration=0.25)
#       pyautogui.moveRel(0, 100, duration=0.25)
#       pyautogui.moveRel(-100, 0, duration=0.25)
#       pyautogui.moveRel(0, -100, duration=0.25)

# 截屏
# im = pyautogui.screenshot()

# 获取某像素坐标的颜色
# print(im.getpixel((50, 200))) # (230, 230, 230)

# 某坐标点像素与颜色是否匹配
# print(pyautogui.pixelMatchesColor(50, 200, (230, 230, 230, 255)))

# 获取图片中心点
# 获取图片位置
# print(list(pyautogui.locateAllOnScreen('star.png')))
# imgLocation = pyautogui.locateOnScreen('star.png')
# print(imgLocation)
# coordination = pyautogui.center(imgLocation)
# print(coordination)

# 获取图片中心点
# print(pyautogui.locateCenterOnScreen('star.png'))

# 自动打印字符串
# pyautogui.click(20, 20)
# pyautogui.typewrite('Hello World!\n')
# pyautogui.typewrite('Hello World!\n', 0.25)
# pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], 0.25)

# 按键名称
# pprint.pprint(pyautogui.KEYBOARD_KEYS)

# Pressing and Releasing the Keyboard
# time.sleep(2)
# pyautogui.keyDown('shift')
# pyautogui.press('2')
# pyautogui.keyUp('shift')

# 等同于
# pyautogui.press('@')

# 热键合并
pyautogui.PAUSE = 1
pyautogui.click(100, 100)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'end')
pyautogui.press('\n')
pyautogui.hotkey('ctrl', 'v')




