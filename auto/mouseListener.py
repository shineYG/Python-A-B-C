from pynput import mouse
import pyautogui


def on_click(x, y, button, pressed):
    # if button == mouse.Button.right:
    #     return False

    # 1、通过 return False 终止事件
    # if x < 50 and y < 50:
    #     return False

    if pressed:
        coordinate = (int(x), int(y))
        pixelColor = pyautogui.screenshot().getpixel(coordinate)
        print(coordinate, pixelColor)

# 2、通过捕获KeyboardInterrupt异常，调用stop 终止
try:
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
except KeyboardInterrupt:
    listener.stop()
