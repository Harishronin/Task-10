"""
 Name : Harish kumar
 Date : 28-Sep-2024
 Program 1 :a.Using x-path and do python selenium automation.
            b.Extract total number of followers and following from guvi official.
 """


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Set up WebDriver 
driver = webdriver.Chrome()

try:
    # Navigate to Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(2)  # Allow time for page to load

    # Log in to Instagram (replace 'your_username' and 'your_password' with actual login credentials)
    username_input = driver.find_element(By.XPATH, "//input[@name='username']")
    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    
    # Enter your Instagram credentials
    username_input.send_keys("your_username")
    password_input.send_keys("your_password")
    password_input.send_keys(Keys.ENTER)
    
    sleep(5)  

    # Go to the specific Instagram page
    driver.get("https://www.instagram.com/guviofficial/")
    sleep(3)  # Allow page to load

    # Extract followers and following using XPath
    # Followers XPath
    followers = driver.find_element(By.XPATH, "//a[contains(@href,'/followers')]/span")
    followers_count = followers.get_attribute('title')  # Get the title attribute for formatted number
    
    # Following XPath
    following = driver.find_element(By.XPATH, "//a[contains(@href,'/following')]/span")
    following_count = following.text  # Directly extract the number of followings

    # Output the results
    print(f"Followers: {followers_count}")
    print(f"Following: {following_count}")

finally:
    # Close the browser
    driver.quit()


