import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import datetime
import jpholiday
import time
import argparse
from default_config import get_default_config


def command_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--headless", action="store_true")
    parser.add_argument("--config_file", type=str, default=None)

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
        self.company_id = login_info["companyid"]
        self.mail = login_info["email"]
        self.password = login_info["password"]

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


def is_holiday(date):
    return date.weekday() >= 5 or jpholiday.is_holiday(date)


if __name__ == '__main__':
    parser = command_options()

    cfg = get_default_config()
    if parser.config_file:
        cfg.merge_from_file(parser.config_file)

    start_time = datetime.time(*cfg.attendance.start)
    end_time = datetime.time(*cfg.attendance.end)

    login_info = cfg.user

    driver_options = driver_options(parser)
    operator = AutoMFKintai(login_info, driver_options)

    operator.login()

    while True:
        dt_now = datetime.datetime.now()
        if is_holiday(datetime.date.today()):  # 平日判断
            continue
        if dt_now.hour == start_time.hour and dt_now.minute == start_time.minute:
            operator.syukkin()
            print(f"{dt_now}出勤しました")
            time.sleep(60)
        elif dt_now.hour == end_time.hour and dt_now.minute == end_time.minute:
            operator.taikin()
            print(f"{dt_now}退勤しました")
            time.sleep(60)
        else:
            time.sleep(30)
