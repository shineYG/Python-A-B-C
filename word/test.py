
from pathlib import Path

# 获取当前目录
current_path = Path.cwd()
print(current_path)

# 输出如下：
# /Users/Anders/Documents/

# 获取Home目录
home_path = Path.home()
print(home_path)

print(Path('.'))
# 输出如下：
# /Users/Anders
