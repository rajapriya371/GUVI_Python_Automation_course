"""Module providingFunction to use webdriver,select the options,time,pytest."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
import pytest


class Test:
    """Class representing a Test"""
    url = "https://www.zenclass.in/class"
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(5)
    driver.maximize_window()

    @pytest.mark.first
    def test_login(self):
        """Function that login into application and verify the title"""
        # locator for username textbox
        xpath1 = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input'
        self.driver.find_element(by=By.XPATH, value=xpath1).send_keys("rajapriya371@gmail.com")
        # locator for password textbox and entering password
        xpath2 = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input'
        self.driver.find_element(by=By.XPATH, value=xpath2).send_keys("India@123")
        # locator for Login and clicking on login button
        xpath3 = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button'
        self.driver.find_element(by=By.XPATH, value=xpath3).click()
        verify = self.driver.title
        assert verify == "Zen Class"
        self.driver.implicitly_wait(5)

    @pytest.mark.second
    def test_data(self):
        """Function clicking on Queries panel and move control to search text box"""
        # locators for queries
        xpath4 = '/html/body/div/div[1]/nav/ul/div[6]/li/span'
        queries = self.driver.find_element(by=By.XPATH, value=xpath4)
        time.sleep(10)
        # clicking on queries
        queries.click()
        time.sleep(10)
        # locator for search text box
        xpath5 = '/html/body/div/div[2]/div/div[1]/div[2]/input'
        search_click = self.driver.find_element(by=By.XPATH, value=xpath5)
        # moving control to search textbox
        search_click.click()
        time.sleep(5)

    @pytest.mark.third
    def test_excel(self):
        """Function extract data from left panel and printing the extracted result"""
        # locator for Extracting all the information from left-hand side ribbon from the portal
        taskname =self.driver.find_elements(by=By.XPATH, value="//div[contains(@class,'ml-4')]")
        mytask = []
        # printing all the information from left-hand side ribbon from the guvi portal
        for task in taskname:
            print(task.text)
            mytask.append(task.text)
        # Exporting all the data to excel
        df_data = pd.DataFrame(mytask)
        df_data.to_excel("Workbook.xlsx", index=False)

    @pytest.mark.fourth
    def test_query(self):
        """Function to raise queries 5 times in the Zen portal"""
        for _ in range(0, 2):
            self.driver.implicitly_wait(15)
            # self.driver.maximize_window()
            # Clicking on create query section
            xpath13 = '//*[@id="root"]/div[2]/div/div[1]/div[1]/button'
            self.driver.find_element(by=By.XPATH, value=xpath13).click()
            self.driver.implicitly_wait(15)
            # locator for cancel button
            xpath6 = '/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]'
            cancel_query = self.driver.find_element(by=By.XPATH, value=xpath6)
            # Clicking on create query section
            cancel_query.click()
            self.driver.implicitly_wait(5)
            # Locators for category dropdown
            xpath7 = '/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
            dropdown1 = self.driver.find_element(by=By.XPATH, value=xpath7)
            # Click on category dropdown
            dropdown1.click()
            dd1 = Select(dropdown1)
            time.sleep(3)
            dd1.select_by_index(1)
            time.sleep(5)
            xpath8 = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'
            # Locators for subcategory dropdown
            dropdown2 = self.driver.find_element(by=By.XPATH, value=xpath8)
            # Clicking on Subcategory dropdown
            dropdown2.click()
            dd2 = Select(dropdown2)
            time.sleep(3)
            dd2.select_by_index(1)
            time.sleep(5)
            # Locators for Preferred Voice Communication Language dropdown
            xpath9 = '/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select'
            dropdown5 = self.driver.find_element(by=By.XPATH, value=xpath9)
            dropdown5.click()
            # Clicking on Preferred Voice Communication Language
            dd5 = Select(dropdown5)
            time.sleep(3)
            dd5.select_by_index(2)
            time.sleep(5)
            # Locators for query title
            xpath10 = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input'
            dropdown3 = self.driver.find_element(by=By.XPATH, value=xpath10)
            # Entering data into Query Title
            query_title = "Guvi Python AT – 1 &2 Automation Project"
            dropdown3.send_keys(query_title)
            time.sleep(5)
            # Locators for Query description
            xpath11 = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea'
            dropdown4 = self.driver.find_element(by=By.XPATH, value=xpath11)
            # Entering data into Query Description
            query_description = "This is a Project Test Code Running for the Python Automation – 1&2 Project Given by mentor Mr. Suman Gangopadhyay."
            dropdown4.send_keys(query_description)
            time.sleep(5)
            # locators for submit button
            xpath12 = '/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button'
            button = self.driver.find_element(by=By.XPATH, value=xpath12)
            # Clicking on submit button
            button.click()
            time.sleep(5)
t = Test()
