from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values
import time
import os


secrets = dotenv_values(".env") # Load instagram credentials from .env file

# Read usernames from file
if os.path.exists("usernames.txt"):
    with open("usernames.txt", "r", encoding="utf-8") as file:
        usernames = [line.strip() for line in file if line.strip()]  # Removes empty lines
    print("usernames.txt file found and loaded successfully.")
else:
    print("Error: usernames.txt not found. Please make sure the file exists.")

# Check if Last_username.txt exists 
if os.path.exists("Last_username.txt"):

    # Read last username that were quit from 
    with open("Last_username.txt", "r", encoding="utf-8") as file:
        last_username = file.readline().strip()  # Removes empty lines
    print("Last_username.txt found and loaded successfully.")

    resume = input("Resume unfollowing from last stop? (y/n): ")

    # Check if the user wants to resume from last stop    
    if resume == "y":

        # Find index of last quit username
        if last_username in usernames:
            start_index = usernames.index(last_username)
        else:
            start_index = 0

        usernames = usernames[start_index:]


else:
    print("Last_username.txt not found.")
   


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
count = 0 # Count of unfollowed users to display during execution 

for insta_username in usernames:
    driver.get(f"https://www.instagram.com/{insta_username}/")
    time.sleep(1)  # Wait for profile page to load

    inp = input("Unfollow? (0/1/q): ")

    if inp == "0":
        pass

    elif inp == "1":
        try:
            # Locate and click "Following" button
            following_button = driver.find_element(By.XPATH, "//button[contains(., 'Following')]")
            following_button.click()
            time.sleep(1)

            # Click "Unfollow" from the popup
            unfollow_button = driver.find_element(By.XPATH, "//span[contains(text(),'Unfollow')]")
            unfollow_button.click()
            print(f"Unfollowed {insta_username}")

            filtered_usernames.append(insta_username)

            count += 1
            print("Count: ", count)
        except:
            print("Error: Not an instagram profile page.")

    elif inp == "q": # Quit

        # Save or update last username
        with open("Last_username.txt", "w", encoding="utf-8") as file:
            file.write("".join(insta_username) + "\n")

        break

    else:
        print("Invalid input.")
        continue

driver.quit()

# Save or update unfollowed usernames
with open("unfollowed_usernames.txt", "a", encoding="utf-8") as file:
        file.write("\n".join(filtered_usernames) + "\n")

print("Total users unfollowed: ", len(filtered_usernames))