# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import os
import time
import sys
import re
import yagmail

me = ["303289379@qq.com"]
yag = yagmail.SMTP(user="3032893795@qq.com", password="nlqczcoxqeeldcid",
                   host="smtp.qq.com", port=465, smtp_ssl=True)
options = Options()
options.headless = True
zhebangniangmen = []
while True:

    driver = webdriver.Firefox(options=options)
    url_liuyan = "https://m.weibo.cn/u/2537019275"

    print("已配置浏览器")
    driver.get(url_liuyan)
    time.sleep(5)
    print("请求微博页...")
    time.sleep(5)
    for ee in range(1, 50):
        driver.find_element_by_css_selector("body").send_keys(Keys.PAGE_DOWN)
        sys.stdout.write("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b" +
                         "正在下拉第" + str(ee) + "次")
        sys.stdout.flush()
    time.sleep(2)
    print("正在采集微博...")
    for x in range(1, 30):
        m = x
        wbs_liuyan = driver.find_elements_by_css_selector(
            "div.card:nth-child("+str(m)+") > div:nth-child(1) > div:nth-child(1) > article:nth-child(2) > div:nth-child(1) > div:nth-child(1)")
        wbs_tu = driver.find_elements_by_css_selector(
            "div.card:nth-child("+str(m)+") > div:nth-child(1) > div:nth-child(1) > article:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li> div:nth-child(1) > img")
        if len(wbs_liuyan) != 0:
            if wbs_liuyan[0].text not in zhebangniangmen:
                zhebangniangmen.append(wbs_liuyan[0].text)
                print(wbs_liuyan[0].text)
                n = 1
                tulist = [wbs_liuyan[0].text]
                for y in wbs_tu:
                    res = requests.get(y.get_attribute('src'))
                    f = open(str(m)+"-"+str(n)+'.jpg', 'wb')
                    f.write(res.content)
                    f.close()
                    tulist.append(str(m)+"-"+str(n)+'.jpg')
                    n += 1
                print(tulist)
                yag.send(to=me, subject="来自Komikado的采集信息",
                            contents=tulist)
    print(str(zhebangniangmen))
    time.sleep(300)
    driver.close()
    time.sleep(3600)
