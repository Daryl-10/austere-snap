from selenium import webdriver
# Version Selenium 4.x
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime
 
from upload import * 


# The following options are required to make headless Chrome
# work in a Docker container
chrome_options = webdriver.ChromeOptions()

# headless gets DENIED when accessing certain websites....
chrome_options.add_argument("--headless")
# comment out --headless argument to "see" the script in action

chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=2048,1440")
chrome_options.add_argument("--no-sandbox")

# to bypass "no-headless-viewing" rule on certain websites
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36")

# Initialize a new browser
browser = webdriver.Chrome(options=chrome_options)

# overview of vessels close to Singapore port marker
url="https://www.vesselfinder.com/?p=SGSIN001"

driver = browser
driver.get(url)
#Give a certain amount of time for the page to load
time.sleep(11)

#To circumvent cookie. Make changes based on target website
try:
    # driver.find_element_by_css_selector('#L2AGLb').click()
    
    #Add additional stages if necessary for various cookie consent forms
    print("Circumvented cookie consent stage 1")
except:
    print("No cookie consent found") 
time.sleep(1)


# set maximum browser size
driver.maximize_window()

time.sleep(1)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div[1]/div[6]/div[3]/div[1]/button[1]')))

# zoom in button
button_zoom_in = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[6]/div[3]/div[1]/button[1]')

# to zoom in (2) times
for i in range(2):
    button_zoom_in.click()
    time.sleep(1)

# load time for map assets to load after zooming in
time.sleep(3)

try:
    # ct stores current date
    ct = datetime.datetime.now().date()
    img_name = "overview_{}.png".format(ct)

    driver.save_screenshot(img_name)
    print("screenshot taken of: ", img_name)
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(1)
# run upload.py function to upload screenshot to Google Drive folder provided
fun_upload()

time.sleep(1)
#Quit driver
driver.quit()