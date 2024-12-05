'''
Author: Archangel 781446156@qq.com
Date: 2024-12-05 14:49:44
LastEditTime: 2024-12-05 16:07:40
LastEditors: Archangel 781446156@qq.com
Description:  
FilePath: \自动化测试\test.py
Copyright (c) 2024 by Archangel email: 781446156@qq.com, All Rights Reserved. 
'''

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


edge_options = EdgeOptions()
edge_options.use_chromium = True  

service = Service(executable_path=r'D:/WebDriver/msedgedriver.exe') 

# 创建Edge浏览器实例
driver = webdriver.Edge(service=service, options=edge_options)

try:
    # 访问百度
    driver.get('https://www.baidu.com')
    time.sleep(2)

    # 找到搜索框并输入查询内容
    search_box = driver.find_element(By.NAME, "wd")
    search_box.send_keys("hello world")
    time.sleep(2)

    # 提交搜索表单
    search_box.submit()

    # 等待页面加载
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#container > div:nth-child(3)"))
    )
    time.sleep(2)
    # 获取前五个搜索结果
    results = driver.find_elements(By.CSS_SELECTOR, '.c-title a')[:5]

    # 打印每个结果的标题和链接
    for index, result in enumerate(results, start=1):
        print(f"{index}: {result.text}")
        print(f"Link: {result.get_attribute('href')}\n")

finally:
    # 关闭浏览器
    driver.quit()
