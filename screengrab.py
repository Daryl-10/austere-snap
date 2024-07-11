from selenium import webdriver
# Version Selenium 4.x
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime
 
from upload import * 

# The following options are required to make headless Firefox
# work in a Docker container
opts = FirefoxOptions()
opts.add_argument("--headless")

# # to bypass "no-headless-viewing" rule on certain websites
# opts.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36")

opts.add_argument("--start-maximized") #open Browser in maximized mode
opts.headless = True
browser = webdriver.Firefox(options=opts)


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

try:
    print("Attempting to zoom in: Timeout in 25 seconds ....")
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div[1]/div[6]/div[3]/div[1]/button[1]')))

    # zoom in button
    button_zoom_in = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[6]/div[3]/div[1]/button[1]')

    print("Zooming in....")
    # to zoom in (4) times
    for i in range(4):
        button_zoom_in.click()
        time.sleep(1)
except:
    print("Unable to zoom. Moving to next step")

# load time for map assets to load after zooming in
time.sleep(3)

print("Closing panel displaying vessel/port information")
# panel close button
button_close_panel = driver.find_element(By.XPATH, '/html/body/main/div[3]/div[1]/div[1]/div[4]')
button_close_panel.click()

# wait before taking screenshot
time.sleep(2)


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