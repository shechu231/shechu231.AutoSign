from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import sys
# 无头浏览器
chrome_options = Options()
# 后面的两个是固定写法 必须这么写 无头浏览器
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
browser.get("https://www.tmooc.cn/")
sleep(10)
browser.find_element_by_id("login_xxw").click()

account=sys.argv[1].split("pwd:")#分开用户账号和密码

browser.find_element_by_id("js_account_pm").send_keys(account[0])
browser.find_element_by_id("js_password").send_keys(account[1])
#js_submit_login
browser.find_element_by_id("js_submit_login").click()
sleep(5)
browser.close()
sleep(2)
# 获取当前所有窗口句柄（窗口A、B）
handles = browser.window_handles
for newhandle in handles:
    browser.switch_to_window(newhandle)
sleep(8)
browser.execute_script('document.querySelector("#studyMsgUl > li.qiandao200310 > div > p.btn.bbb1").click()')
sleep(2)
print("签到成功")
browser.quit()
