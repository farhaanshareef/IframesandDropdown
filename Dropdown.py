import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

class DropDown:
    def __init__(self, driver):
        self.driver = driver

    def switch_frame(self):
        try:
           # Switch to the notification frame and close the notification
           frame = WebDriverWait(self.driver, 10).until(
             EC.frame_to_be_available_and_switch_to_it("notification-frame-173061603"))

           cross_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[@id='webklipper-publisher-widget-container-notification-close-div'])[1]")))
           cross_button.click()
        except:
            pass

    def select_suggestion(self, suggestion_index):
        suggestions = self.driver.find_elements(By.CLASS_NAME, 'react-autosuggest__suggestion')
        time.sleep(2)
        suggestions[suggestion_index].click()

    def test_drop_down(self):

        self.switch_frame()
        # Click on the "From" city input field
        from_city = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'fromCity')))
        from_city.click()

        # Enter the text for the "From" city
        from_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'react-autosuggest__input--open')))
        from_text.send_keys('PAK')

        # Wait for the suggestion list to appear and print its data
        suggestion_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'react-autosuggest__suggestions-list')))
        print(len(suggestion_list))
        print("From Suggestion list countries are ")
        for suggestionslist in suggestion_list:
            print(suggestionslist.text)

        # Select the desired suggestion from the suggestion list
        self.select_suggestion(4)

        # Click on the "To" city input field
        to_city = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'toCity')))
        to_city.click()

        # Enter the text for the "To" city
        to_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='To']")))
        to_text.send_keys('Dubai')

        # Wait for the suggestion list to appear and print its data
        to_suggestion_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'react-autosuggest__suggestions-list')))
        print(len(to_suggestion_list))
        print("To Suggestion list countries are ")
        for suggestionslist in to_suggestion_list:
            print(suggestionslist.text)

        # Select the desired suggestion from the suggestion list
        self.select_suggestion(0)

        # Get today's date and format it to match the desired format
        today = datetime.today().strftime("%a %b %d %Y")  # e.g., Fri Jun 09 2023
        current_date = datetime.today().strftime("%d")

        # Construct the dynamic CSS locator based on today's date
        css_locator = f"div[aria-label='{today}'] p:nth-child(1)"

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_locator))).click()

        # Click the search button
        search_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Search')]")))
        search_btn.click()

        try:
            # Wait up to 20 seconds for the element to be visible
            popular_filter_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Popular Filters']")))
            # Assert that the element is visible
            assert popular_filter_text.is_displayed(), "Element is not visible"
            print("Element is visible. Test case passed!")
        except TimeoutException:
            # Element is not visible within the given timeout
            print("Element is not visible. Test case failed!")

#setting up the browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the website and maximize the window
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
dropdown = DropDown(driver)
dropdown.test_drop_down()
