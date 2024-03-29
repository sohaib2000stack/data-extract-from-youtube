from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver executable
chrome_driver_path = "C:/Program Files (x86)/chromedriver.exe"

# Initialize the WebDriver
driver = webdriver.Chrome(service=chrome_driver_path)

# Open YouTube
driver.get("https://www.youtube.com/")

# Find the search box and input the keyword
keyword = 'Atif Aslam'
search_box = driver.find_element("name", "search_query")
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(5)

# Find and print the titles of the top 10 videos
video_titles = driver.find_elements_by_xpath('//a[@id="video-title"]')

for i, title in enumerate(video_titles[:10], 1):
    print(f"{i}. {title.get_attribute('title')}")

# Close the WebDriver
driver.quit()
