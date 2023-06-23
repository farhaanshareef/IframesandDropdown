from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class IFrame:
    def __init__(self, driver):
        self.driver = driver

    def switch_frame(self):

        #setting up the browser
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Open the website and maximize the window
        driver.get("https://www.zameen.com/")
        driver.maximize_window()

        # Define the frame and close button locators
        frame_locator = "google_ads_iframe_/31946216/Splash_660x500_0"
        close_button_locator = (By.CLASS_NAME, "close_cross_big")

        # Switch to the frame
        iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))

        # Click on the cross icon and close the frame
        close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(close_button_locator)).click()

        # Switch back to default content
        driver.switch_to.default_content()

iframe= IFrame(webdriver)
iframe.switch_frame()
