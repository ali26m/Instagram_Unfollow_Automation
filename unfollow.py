from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values
import time


secrets = dotenv_values(".env") # Load instagram credentials from .env file

# Read usernames from file
with open("usernames.txt", "r", encoding="utf-8") as file:
    usernames = [line.strip() for line in file if line.strip()]  # Removes empty lines

# Read last username that were quit from 
with open("Last username.txt", "r", encoding="utf-8") as file:
    last_username = file.readline().strip()  # Removes empty lines

resume = input("Resume unfollowing from last stop? (y/n): ")

if resume == "y":

    # Find index of last quit username
    if last_username in usernames:
        start_index = usernames.index(last_username) + 1
    else:
        start_index = 0

    usernames = usernames[start_index:]

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
time.sleep(9)  # Wait for login

filtered_usernames = [] # List of unfollowed usernames
remaining_usernames = [] # List of followed usernames that dont follow back
count = 0 # Count of unfollowed users to display during execution 

for insta_username in usernames:
    driver.get(f"https://www.instagram.com/{insta_username}/")
    time.sleep(1)  # Wait for profile page to load

    inp = input("Unfollow? (0/1/q): ")

    if inp == "0":
        remaining_usernames.append(insta_username)
        pass

    elif inp == "1":
        filtered_usernames.append(insta_username)

        count += 1
        print("Count: ", count)

        # Locate and click "Following" button
        following_button = driver.find_element(By.XPATH, "//button[contains(., 'Following')]")
        following_button.click()
        time.sleep(1)

        # Click "Unfollow" from the popup
        unfollow_button = driver.find_element(By.XPATH, "//span[contains(text(),'Unfollow')]")
        unfollow_button.click()
        print(f"Unfollowed {insta_username}")

    elif inp == "q": # Quit

        # Save or update last username
        with open("Last username.txt", "w", encoding="utf-8") as file:
            file.write("".join(insta_username) + "\n")

        break

    else:
        print("Invalid input")
        continue

driver.quit()

# Save or update unfollowed usernames
with open("unfollowed_usernames.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(filtered_usernames) + "\n")

print("total users unfollowed: ", len(filtered_usernames))