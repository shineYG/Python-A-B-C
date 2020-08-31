import subprocess
import webbrowser

# - 打开电脑程序
# subprocess.run(['start', 'D:\\Development\\PyCharm\\bin\\pycharm64.exe'], shell=True)

# - 打开文本
# subprocess.run(['start', 'D:\\python-demo\\boy_1.txt'], shell=True)

# - 执行shell命令， 在idle中需要添加 stdout=subprocess.PIPE
# subprocess.run(['dir', 'D:\\python-demo'], shell=True, stdout=subprocess.PIPE)
subprocess.run(['dir', 'D:\\python-demo'], shell=True)

# - 打开网页
# webbrowser.open('www.baidu.com')