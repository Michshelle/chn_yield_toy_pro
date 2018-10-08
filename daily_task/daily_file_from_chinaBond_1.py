#!/usr/bin/python3

from selenium import webdriver
from datetime import datetime,timedelta
import time




chr_driver = webdriver.Chrome('/usr/local/bin/chromedriver')

today = datetime.today().strftime('%Y-%m-%d')

requesting = 'http://yield.chinabond.com.cn/cbweb-mn/yc/downBzqxDetail?ycDefIds=2c9081e50a2f9606010a3068cae70001&&zblx=txy&&workTime={}&&dxbj=0&&qxlx=0,&&yqqxN=N&&yqqxK=K&&wrjxCBFlag=0&&locale=zh_CN'.format(today)

chr_driver.get(requesting)
chr_driver.close()





#chr_driver.get('https://www.baidu.com')
