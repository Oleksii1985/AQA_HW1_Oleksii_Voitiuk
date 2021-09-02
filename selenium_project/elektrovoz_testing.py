import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


def test_01():
    chrome_driver_path = Chrome("C:/Users/Admin/PycharmProjects/AQA_HW1_Oleksii_Voitiuk/"
                                "selenium_project/drivers/chromedriver.exe")
    search_input_field_locator = "//input[@placeholder='Что вы ищете?']"
    first_link_in_search_locator = "//div[@class='product_preview__name']/a[1]"

    chrome_driver_path.get("https://elektrovoz.com.ua/")
    chrome_driver_path.maximize_window()

    search_input_field: WebElement = chrome_driver_path.find_element_by_xpath(search_input_field_locator)
    search_input_field.send_keys("розетки")
    time.sleep(3)
    search_input_field.send_keys(Keys.ENTER)
    time.sleep(3)

    first_link: WebElement = chrome_driver_path.find_element_by_xpath(first_link_in_search_locator)
    first_link.click()

    time.sleep(5)
    chrome_driver_path.quit()
