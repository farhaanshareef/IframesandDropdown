import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

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

# Click on the "From" city input field
from_city = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'fromCity')))
from_city.click()

# Enter the text for the "From" city
from_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'react-autosuggest__input--open')))
from_text.send_keys('PAK')

# Wait for the suggestion list to appear and print its data
suggestion_list = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'react-autosuggest__suggestions-list')))
print(len(suggestion_list))
print("From Suggestion list countries are ")
for suggestionslist in suggestion_list:
    print(suggestionslist.text)

# Select the desired suggestion from the suggestion list
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-autosuggest__suggestion')))
click_isb= driver.find_elements(By.CLASS_NAME, 'react-autosuggest__suggestion')
time.sleep(2)
click_isb[4].click()

# Click on the "To" city input field
to_city = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'toCity')))
to_city.click()

# Enter the text for the "To" city
to_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='To']")))
to_text.send_keys('Dubai')

# Wait for the suggestion list to appear and print its data
to_suggestion_list = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'react-autosuggest__suggestions-list')))
print(len(to_suggestion_list))
print("To Suggestion list countries are ")
for suggestionslist in to_suggestion_list:
    print(suggestionslist.text)

# Select the desired suggestion from the suggestion list
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-autosuggest__suggestion')))
to_city_name= driver.find_elements(By.CLASS_NAME, "react-autosuggest__suggestion")
time.sleep(2)
to_city_name[0].click()

# Get today's date and format it to match the desired format
today = datetime.today().strftime("%a %b %d %Y")  # e.g., Fri Jun 09 2023
current_date = datetime.today().strftime("%d")

# Construct the dynamic css locator on the basis of today's date
css_locator= f"div[aria-label='{today}'] p:nth-child(1)"

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_locator))).click()

# Click the search button
search_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Search')]")))
search_btn.click()

try:
    # Wait up to 20 seconds for the element to be visible
    popular_filter_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Popular Filters']")))
    # Assert that the element is visible
    assert popular_filter_text.is_displayed(), "Element is not visible"
    print("Element is visible. Test case passed!")
except TimeoutException:
    # Element is not visible within the given timeout
    print("Element is not visible. Test case failed!")