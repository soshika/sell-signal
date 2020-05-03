# -*- coding: utf-8 -*-

from time import sleep
from datetime import datetime
from selenium import webdriver
import telegram


def is_expired(now):
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
        # if is_expired(now):
        #     print('robot is shutdown at: ', now)
        #     break

    stocks = [

    ]

    contacts = [

    ]

    for stock in stocks:
        driver = webdriver.Chrome(executable_path='')
        driver.get(stock[0])

        print('robot is taking nap for 10 seconds!')
        sleep(10)

        buy_amount = int(str(driver.find_element_by_xpath('//*[@id="leftColumn"]/div[1]/div/app-queue-and-legal-real/div/div[1]/app-queue-table/div/div[1]/table/tbody/tr[2]/td[2]/span').text).replace(',', ''))
        buy_count = int(str(driver.find_element_by_xpath('//*[@id="leftColumn"]/div[1]/div/app-queue-and-legal-real/div/div[1]/app-queue-table/div/div[1]/table/tbody/tr[2]/td[1]/span').text).replace(',', ''))

        sell_amount = int(str(driver.find_element_by_xpath('//*[@id="leftColumn"]/div[1]/div/app-queue-and-legal-real/div/div[1]/app-queue-table/div/div[2]/table/tbody/tr[2]/td[2]/span').text).replace(',', ''))
        sell_count = int(str(driver.find_element_by_xpath('//*[@id="leftColumn"]/div[1]/div/app-queue-and-legal-real/div/div[1]/app-queue-table/div/div[2]/table/tbody/tr[2]/td[3]/span').text).replace(',', ''))

        driver.close()

        sell = sell_amount * sell_count
        buy = buy_count * buy_amount

        print('sell is: ', sell)
        print('buy is: ', buy)

        if sell >= buy:
            ####################
            # Use Telegram API #
            ####################

            for contact in contacts:
                message = '{}, time comes to sell {} right now!'.format(contact[1], stock[1])
                telegram.send_message(contact[0], message)

        else:
            for contact in contacts:
                message = "Don't rush {}, just save the {}".format(contact[1], stock[1])
                telegram.send_message(contact[0], message)


if __name__ == '__main__':
    main()
