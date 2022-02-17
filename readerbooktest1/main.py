# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.common.appiumby import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from uiautomator2 import connect
# 导入 uiautomator2 的包并进行实例化
driver = connect()  # 连接手机
print(driver.info)  # 为你的手机安装一个ATX进程守护工具

driver.swipe()
"""
POM： page  Object model 页面配置模型
1. Bagepage： 项目中所有需要做自动化的页面都封装到类中，一个页面对应一个类，Selenium的原生方法，定位元素，跳转框架，处理下拉框
2. PO页面层：  页面对象层，把一个一个的页面封装成类
3. 测试用例层： 测试用例的业务逻辑及数据驱动
它们之间的关系： 第二层PO层 继承第一层Bagepage基础层，第三层测试用例调用第二层里面的方法

"""


desired_caps = {
  "platformName": "Android",             # 所连接的手机设备系统名称
  "platformVersion": "10.0.0",           # 所连接的手机设备型号
  "deviceName":"ANP0220528001775",       # 所连接的手机设备名称
  "appPackageName":"com.zhao.myreader",  # app的包名
  "appActivity":"com.zhao.myreader.ui.home.MainActivity", # app活动名
  "NewCommandTimeout": 10                # appium 默认超时时间为60s，若在默认时间范围内没有找到元素，自动关闭session，后面的操作就会报错，通过NewCommandTimeout 自定义超时时间，单位为秒；

}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)


# 隐式等待(全局资源等待)：driver.implicitly_wait(time),其中time为number类型,(int+float)
driver.implicitly_wait(10.05)
# activity 等待,切换activity时，等待新activity加载时间范围为10s
driver.wait_activity(".home.MainActivity",10)
# time.sleep(10) 显性等待，可以直接等待已经显示在界面中的元素，可以不用在判断is.display()
WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.ACCESSIBILITY_ID,"书城")).click()

element1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,
'//*[@resource-id="com.zhao.myreader:id/ll_no_data_tips"]/android.widget.ImageView[1]')))
