# -*- coding: utf-8 -*-

from time import sleep
from datetime import datetime
from selenium import webdriver


def isExpired(now):
    if now.hour > 12:
        return True
    if now.hour == 12 and now.minute > 30:
        return True
    if now.hour <= 8:
        return True


def main():
    now = datetime.now()
    print("robot is up & running at: ", now)

    while True:
        now = datetime.now()
        if isExpired(now):
            print('robot is shutdown at: ', now)
            break

    urls = [
        'https://www.sahamyab.com/hashtag/غگرجی/post',
        'https://www.sahamyab.com/hashtag/بورس',
        'https://www.sahamyab.com/hashtag/کالا',
        'https://www.sahamyab.com/hashtag/درهآور',
        'https://www.sahamyab.com/hashtag/تکشا',
        'https://www.sahamyab.com/hashtag/داوه',
        'https://www.sahamyab.com/hashtag/غگیلا',
        'https://www.sahamyab.com/hashtag/سفاسی'
    ]

    for url in urls:
        driver = webdriver.Chrome(
            executable_path='/Users/soshika/Documents/dev/python3/stocks/sell-signal/chromedriver')
        driver.get(url)

        title = driver.find_element_by_xpath(
            '/html/body/div[1]/app-root/div/main/div/div/app-symbol-detail/div[2]/div[2]/div/table/td[1]/div/h1').text
        print(title)

        driver.close()


if __name__ == '__main__':
    main()
