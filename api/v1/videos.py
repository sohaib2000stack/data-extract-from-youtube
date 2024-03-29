from fastapi import APIRouter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

router = APIRouter()
# router = APIRouter()

# @router.get("/")
# async def get_videos():
#     # Your implementation here
#     pass
@router.get("/videos/")
def get_videos_v1(keyword: str):
    # Setup the Chrome driver
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    # Open YouTube
    driver.get("https://www.youtube.com/")

    # Find the search box and input the keyword
    search_box = driver.find_element("name", "search_query")
    search_box.send_keys(keyword)
    search_box.submit()

    # Wait for the search results to load
    time.sleep(5)

    # Find and print the titles of the top 10 videos
    video_titles = driver.find_elements(by='id', value="video-title")
    titles = [title.get_attribute('title') for title in video_titles[:10]]

    # Close the browser
    driver.quit()

    return {"keyword": keyword, "titles": titles}
