import pyautogui, time

print('Press Ctrl+C to quit. ')

positionStr = ''
try:
    while True:
        time.sleep(2)

        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr = 'X: {:4};  Y: {:4};  RGB: {}'.format(x, y, pixelColor)
        print(positionStr)

except KeyboardInterrupt:
    print('\nDone. ')