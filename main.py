import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"
SPEED_TEST_URL = "https://www.speedtest.net/"

REGULAR_DOWNLOAD_SPEED = 600
REGULAR_UPLOAD_SPEED = 400


def send_twitter(low_download_speed, low_upload_speed):
    text = f"Dear @testInternetProvider why my download speed is {low_download_speed} when it is supposed to be 600MB" \
           f" and my upload speed is {low_upload_speed} when it is supposed to be 400MB?"

    twitter_driver = webdriver.Chrome()
    twitter_driver.get(TWITTER_LOGIN_URL)

    twitter_driver.implicitly_wait(5)
    time.sleep(1)
    name_input = twitter_driver.find_element(By.NAME, "text")
    name_input.send_keys("ederROBOT")

    button_next = twitter_driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    button_next.click()

    twitter_driver.implicitly_wait(5)
    time.sleep(3)
    password_input = twitter_driver.find_element(By.NAME, "password")
    password_input.send_keys("Eder@teste321")
    password_input.send_keys(Keys.ENTER)

    twitter_driver.implicitly_wait(5)
    time.sleep(3)
    twitter_text_box = twitter_driver.find_element(By.CSS_SELECTOR, ".public-DraftEditor-content")
    twitter_text_box.send_keys(text)

    send_twitter_text_button = twitter_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
    send_twitter_text_button.click()
    twitter_driver.implicitly_wait(2)
    time.sleep(2)


valid = False

while not valid:
    speed_driver = webdriver.Chrome()
    speed_driver.get(SPEED_TEST_URL)

    speed_driver.implicitly_wait(5)
    time.sleep(5)
    go_button = speed_driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
    go_button.click()

    speed_driver.implicitly_wait(60)
    time.sleep(60)

    download_speed = speed_driver.find_element(By.CSS_SELECTOR, ".download-speed").text
    upload_speed = speed_driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

    print(f"DOWNLOAD SPEED = {download_speed}")
    print(f"UPLOAD SPEED = {upload_speed}")

    download_speed = float(download_speed)
    upload_speed = float(upload_speed)

    if download_speed is None or upload_speed is None:
        valid = False
    else:
        valid = True
        if download_speed < REGULAR_DOWNLOAD_SPEED or upload_speed < REGULAR_UPLOAD_SPEED:
            print("INTERNET SLOW")
            send_twitter(download_speed, upload_speed)
        else:
            print("INTERNET IS GOOD")
            send_twitter(download_speed, upload_speed)