# whatsapp_spammer.py

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login_whatsapp(phone_number, message):
    # Set up the WebDriver
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get('https://web.whatsapp.com')
    time.sleep(10)  # Wait for the user to scan the QR code

    # Input phone number
    search_box = driver.find_element_by_xpath('//input[@placeholder="Search or start new chat"]')
    search_box.send_keys(phone_number)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Send message
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="7"]')
    for _ in range(1000000):
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
        time.sleep(random.uniform(0.1, 1))  # Add random delay to avoid detection

    # Close the browser
    driver.quit()

def main():
    phone_number = input("Enter the phone number to send messages from: ")
    message = input("Enter the message to send: ")
    login_whatsapp(phone_number, message)

if __name__ == "__main__":
    main()
