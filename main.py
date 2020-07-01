import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import datetime
import jpholiday
import time
import argparse


def command_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--headless", type=bool, default=False)

    return parser.parse_args()


def driver_options(parser):
    options = Options()
    if parser.headless:
        options.add_argument("--headless")

    return options


class AutoMFKintai():
    def __init__(self, login_info, driver_options):
        URL = "https://attendance.moneyforward.com/my_page"
        driver = webdriver.Chrome(options=driver_options)
        driver.set_window_size(*(960, 540))
        driver.get(URL)
        self.driver = driver
        self.company_id = login_info["COMPANY_ID"]
        self.mail = login_info["MAIL"]
        self.password = login_info["PASSWORD"]

    def login(self):
        id_box = self.driver.find_element_by_name("employee_session_form[office_account_name]")
        id_box.send_keys(self.company_id)

        mail_box = self.driver.find_element_by_name("employee_session_form[account_name_or_email]")
        mail_box.send_keys(self.mail)

        password_box = self.driver.find_element_by_name("employee_session_form[password]")
        password_box.send_keys(self.password)

        login_button = self.driver.find_element_by_name("commit")
        login_button.click()

    def syukkin(self):
        try:
            actions = ActionChains(self.driver)
            actions.move_by_offset(480, 250)
            actions.click()
            actions.perform()
        except selenium.common.exceptions.MoveTargetOutOfBoundsException:
            pass

    def taikin(self):
        try:
            actions = ActionChains(self.driver)
            actions.move_by_offset(600, 250)
            actions.click()
            actions.perform()
        except selenium.common.exceptions.MoveTargetOutOfBoundsException:
            pass

    def release(self):
        self.driver.quit()


def is_weekday(date):
    if date.weekday() >= 5 or jpholiday.is_holiday(date):
        return False
    else:
        return True


if __name__ == '__main__':
    parser = command_options()

    start_time = datetime.time(10, 0)
    end_time = datetime.time(18, 45)

    with open("pass.txt") as f:
        login_info = dict()
        login_info["COMPANY_ID"] = f.readline().rstrip()
        login_info["MAIL"] = f.readline().rstrip()
        login_info["PASSWORD"] = f.readline().rstrip()

    driver_options = driver_options(parser)
    operator = AutoMFKintai(login_info, driver_options)

    operator.login()

    while True:
        dt_now = datetime.datetime.now()
        if not is_weekday(datetime.date.today()):  # 平日判断
            continue
        if dt_now.hour == start_time.hour and dt_now.minute == start_time.minute:
            operator.syukkin()
        elif dt_now.hour == end_time.hour and dt_now.minute == end_time.minute:
            operator.taikin()
        else:
            time.sleep(30)
