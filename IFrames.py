from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s= Service("//Users//mac//Downloads//chromedriver_mac_arm64")

# create webdriver object
driver = webdriver.Chrome(service=s)

# Open the website and maximize the window
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

# Switch to the notification frame and close the notification
frame = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("notification-frame-173061603"))

cross_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@id='webklipper-publisher-widget-container-notification-close-div'])[1]")))
cross_button.click()

#switch back to default content
driver.switch_to.default_content()