# coding=utf-8

import os
from selenium import webdriver

#知乎的用户名和密码
username = ""
password = ""

#，获取浏览器的驱动，这里需要提前给firefox指定环境变量，如果没有指定则需要指定路径
driver = webdriver.Firefox()

#窗口最大化
driver.maximize_window()

#打开登录页面
driver.get("https://www.zhihu.com/signup?next=%2F")

#切换到登录页面
driver.find_element_by_class_name('SignFlow-tab--active').click()

#给输入框赋值
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(username)
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(password)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)

#模拟点击事件
driver.find_element_by_tag_name('button').click()

print(driver.title)
os.system("pause")