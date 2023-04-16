# automatic-umbrella

Scrapes dedicated Reddit images

Automatic Umbrella is a Python script that uses the Reddit API to scrape images from subreddits. The script collects up to 2000 images, stores them in a folder, and outputs an Excel file containing the image name, post title, and user who posted the image.

## Setup

Follow these steps to set up and use the Home Maintenance Scraper:

### Step 1: Create a Reddit API Application

1. Log in to your Reddit account and go to the App Preferences page.
2. Click on the "Create App" or "Create Another App" button at the bottom of the page.
3. Fill out the form with the following details:
    a. "name": Give your application a name, e.g., "automatic-umbrella".
    b. "App type": Select "script".
    c. "description": Add a brief description of your application (optional).
    d. "about url" and "redirect uri": Leave these fields blank, as they're not required for a script app.
    e. "permissions": Leave the default permissions selected.
4. Click "Create App".
5. Note down the "client_id" (located under "web app" on the app's detail page) and "client_secret".

### Step 2: Install the Required Libraries

Install the required Python libraries (praw, requests, openpyxl, and Pillow) by running:

```bash
pip install praw requests openpyxl Pillow
```

### Step 3: Set Up the Script
1. Download the automatic-umbrella.py script from this repository.
2. Open the script in a text editor and replace the following placeholders with your Reddit API credentials and user information:
 a. <your_new_client_id>: Replace with the client ID from your Reddit API application.
 b. <your_new_client_secret>: Replace with the client secret from your Reddit API application.
 c. <your_user_agent>: Replace with a custom user agent string (e.g., python:automatic-umbrella:1.0 (by /u/YourRedditUsername)).
 d. <your_reddit_username>: Replace with your Reddit username.
 e. <your_reddit_password>: Replace with your Reddit password.
  
### Step 4: Run the Script
  Run the script using Python:
```bash
python home_maintenance_scraper.py
 ```
The script will scrape images from the specified subreddits, save them in a folder called HomeMaintenance_images, and create an Excel file called HomeMaintence.xlsx containing the image name, post title, and user who posted the image.
 
### Step 5: Usage
 
You can customize the subreddits to scrape by modifying the subreddit variable in the script. Replace "HomeMaintenance" with the desired subreddit name:
```bash
subreddit = reddit.subreddit("DesiredSubreddit")
```
To scrape multiple subreddits, you can use the "+" operator to combine subreddit names:
```bash
subreddit = reddit.subreddit("Subreddit1+Subreddit2+Subreddit3")
```
Make sure to follow the API terms and conditions and respect the community guidelines of each subreddit when scraping content. Additionally, adhere to the rules and limits imposed by Reddit's API, such as rate limits and user agent requirements.
