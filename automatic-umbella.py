import praw
import os
import requests
from openpyxl import Workbook
from PIL import Image

# Set up the Reddit API client
client_id = ""
client_secret = "" 
user_agent = ""  #name of the script 
username = ""
password = ""

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password,
)

# Create a folder to store the images
image_folder = "HomeMaintenance_images"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Create an Excel file and set up the header row
workbook = Workbook()
worksheet = workbook.active
worksheet.append(["Image Name", "Title", "User"])

# Scrape images from r/HomeMaintenance. Simply changge to subreddit of choice
subreddit = reddit.subreddit("HomeMaintenance")
count = 0
for submission in subreddit.new(limit=1000):
    if submission.url.endswith((".jpg", ".jpeg", ".png")):
        count += 1
        print(f"Processing image {count}: {submission.url}")

        # Download the image
        response = requests.get(submission.url)
        image_name = f"{count}_{submission.id}.{submission.url.split('.')[-1]}"
        image_path = os.path.join(image_folder, image_name)
        with open(image_path, "wb") as f:
            f.write(response.content)

        # Verify the image and remove if invalid
        try:
            Image.open(image_path).verify()
        except IOError:
            print(f"Invalid image: {image_path}")
            os.remove(image_path)
            count -= 1
            continue

        # Add the image details to the Excel file. If you would like to add the user's name tied just add submission.user. Some users are deleted and will throw out an error, keep that in mind. 
        worksheet.append([image_name, submission.title])

        # Stop after 2000 valid images
        if count == 2000:
            break

# Save the Excel file
workbook.save("HomeMaintenance.xlsx")
print("Scraping completed.")
