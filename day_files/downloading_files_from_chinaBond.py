from selenium import webdriver
from datetime import datetime,timedelta
import time




chr_driver = webdriver.Chrome('/usr/local/bin/chromedriver')
end_date = '2018-10-10'
start_date = '2018-10-01'

endDate = datetime.strptime(end_date,'%Y-%m-%d')
startDate = datetime.strptime(start_date,'%Y-%m-%d')


while startDate <= endDate:

    today = startDate.strftime('%Y-%m-%d')
    startDate += timedelta(days=1)

    requesting = 'http://yield.chinabond.com.cn/cbweb-mn/yc/downBzqxDetail?ycDefIds=2c9081e50a2f9606010a3068cae70001&&zblx=txy&&workTime={}&&dxbj=0&&qxlx=0,&&yqqxN=N&&yqqxK=K&&wrjxCBFlag=0&&locale=zh_CN'.format(today)

    chr_driver.get(requesting)
    time.sleep(1.02)
    print(today)




#chr_driver.get('https://www.baidu.com')
