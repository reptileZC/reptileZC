# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re
# from bs4 import BeautifulSoup
# import pymongo
# from selenium.common.exceptions import TimeoutException
#
#
# KEYWORD='美食'
# browser = webdriver.Chrome()#声明浏览器
# wait = WebDriverWait(browser,10)#显式延时等待
#
#
# def get_search():
#     url = 'https://www.taobao.com'#首页的url
#     browser.get(url)#输入url
#     try:
#         # 查找搜索框的节点，判断搜索框是否已经加载好
#         inputs = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
#         #查找搜索按钮，判断是否已经具备点击功能
#         button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
#         inputs.send_keys(KEYWORD)#输入搜索的关键字
#         button.click()#点击按钮
#         # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager .wraper .inner.clearfix')))
#         #判断页面是否已经加载好，并提取页码信息
#         page=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))).text.strip()
#         page = re.search('\d+',page).group()
#         get_information(browser.page_source)#提取当前页的信息
#         return int(page)
#     except TimeoutException:
#         print('get_search()出现TimeoutException')
#         return get_search()


from selenium import webdriver
import time

#   打开课工场网站主页【第一个窗口】
driver = webdriver.Chrome()
driver.get('http://www.kgc.cn/')
driver.maximize_window()

#   点击全部课程，进入课程库【第二个窗口】
driver.find_element_by_link_text('全部课程').click()
time.sleep(3)

#   使用第一种方法切换浏览器【切换到第二个窗口】
windows = driver.window_handles
driver.switch_to.window(windows[0])
time.sleep(3)