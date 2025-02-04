# Instagram Unfollow Automation

A Python script to automate the process of unfollowing users on Instagram with just two buttons.

## Features
- Automates the unfollowing process on Instagram.
- Saves progress to resume from where you left off.
- Provides an interactive experience to choose whether to unfollow or skip a user.
- Display the number of unfollowed users
- Stores the list of unfollowed users and the last processed username. 

## Setup
1. Create a `.env` file in the project directory and add your Instagram credentials (do not share your `.env` to anyone):
   ```env
   INSTAGRAM_USERNAME="your_username"
   INSTAGRAM_PASSWORD="your_password"
   ```
2. Create a `usernames.txt` file in the same directory and list the usernames you want to unfollow (one per line).
   - You can use the Instagram feature to download your data and information to a file and use it. you can see the instructions of downloading a copy of your information in Accounts Center [here](https://help.instagram.com/181231772500920?helpref=faq_content#download-a-copy-of-your-information-in-accounts-center). Choose wheather you want to download all your data or just the `followers and following` data for this script.
   - After downloading the zip file and exporting the files go to [comparetwolists.com](https://comparetwolists.com/) and upload `following.html` into List A and `followers_1.html` into List B, then check the Instagram followers checkbox and hit compare lists.
   - the lists will be displayed. The list `Only in list A` contains the usernames that you follow the but they didn't follow you back. download it and rename it to `usernames.txt` to move it with the Python script.

## Usage
Run the script using:
```
python unfollow.py
```

### Script Workflow
1. The script will ask if you want to resume from the last processed username:
   > Resume unfollowing from last stop? (y/n): 
   - Enter `y` (yes) to continue from where you left off.
   - Enter `n` (no) to start from the beginning.
3. A browser window will open, logging into your Instagram account automatically.
4. The script will go through the list of usernames and prompt you with:
   > Unfollow? (0/1/q):
   - **0**: Skip the user and don't unfollow.
   - **1**: Unfollow the user.
   - **q**: Quit the execution and save progress.
5. The script will generate two files:
   - `unfollowed_usernames.txt` → Contains the list of users you have unfollowed.
   - `Last_username.txt` → Stores the last processed username to resume later.

## Note:
- Test the code multiple times to adjust the sleep time based on your internet connection.
- Give at least one second more after the webpage has loaded.
- Example: For Instagram login, it takes longer than other processes for validation and authentication.
  > time.sleep(9)

## Demo Video:


# Thank You



This script is meant for educational purposes only. You can use it at your own risk.
