from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values
import time
import os


secrets = dotenv_values(".env") # Load instagram credentials from .env file

# Read usernames from file
if os.path.exists("requests.txt"):
    with open("requests.txt", "r", encoding="utf-8") as file:
        usernames = [line.strip() for line in file if line.strip()]  # Removes empty lines
    print("requests.txt file found and loaded successfully.")
else:
    print("Error: requests.txt not found. Please make sure the file exists.")   

# Check if Last_username.txt exists 
if os.path.exists("Last_unrequested_username.txt"):

    # Read last username that were quit from 
    with open("Last_unrequested_username.txt", "r", encoding="utf-8") as file:
        last_username = file.readline().strip()  # Removes empty lines
    print("Last_unrequested_username.txt found and loaded successfully.")

    resume = input("Resume unrequesting from last stop? (y/n): ")

    # Check if the user wants to resume from last stop    
    if resume == "y":

        # Find index of last quit username
        if last_username in usernames:
            start_index = usernames.index(last_username)
        else:
            start_index = 0

        usernames = usernames[start_index:]

else:
    print("Last_unrequested_username.txt not found.")


# Instagram login process
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# -------------------------------------------------------------
# Adjust the sleep time based on your internet connection
# -------------------------------------------------------------

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)  # Wait for the login page to load

# Enter username and password
driver.find_element(By.NAME, "username").send_keys(secrets["INSTAGRAM_USERNAME"])
driver.find_element(By.NAME, "password").send_keys(secrets["INSTAGRAM_PASSWORD"] + Keys.RETURN)
time.sleep(50)  # Wait for login

count = 0 # Count of unfollowed users to display during execution 

for insta_username in usernames:
    driver.get(f"https://www.instagram.com/{insta_username}/")
    time.sleep(3)  # Wait for profile page to load

    try:
        # Locate and click "Following" button
        following_button = driver.find_element(By.XPATH, "//button[contains(., 'Requested')]")
        following_button.click()
        time.sleep(1.5)
        
        # Locate and click "Unfollow" button
        following_button = driver.find_element(By.XPATH, "//button[contains(., 'Unfollow')]")
        following_button.click()
        time.sleep(2)

        print(f"unrequest {insta_username}")

        count += 1
        print("Count: ", count)

    except Exception as e:
        print("Error: ", e)

    finally:
        # Save or update last username
        with open("Last_unrequested_username.txt", "w", encoding="utf-8") as file:
            file.write("".join(insta_username) + "\n")


driver.quit()


print("Total users unfollowed: ", count)