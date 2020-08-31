import time, subprocess

timeLeft = 5

while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

print('Music, Now! ')
subprocess.run(['start', 'C:\\Users\\yangg\\Music\\Bharatt-Saurabh-Mila-Jo-Tu.mp3'], shell=True)