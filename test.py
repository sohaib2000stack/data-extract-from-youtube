from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from transformers import pipeline
import time

def get_video_titles(keyword: str):
    # Setup the Chrome driver
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    try:
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

        # Initialize BERT sentiment analysis pipeline
        sentiment_analysis = pipeline("sentiment-analysis")

        # Print the titles and analyze sentiment using BERT
        for title in titles:
            print(title)
            sentiment_result = sentiment_analysis(title)[0]
            print(f'Sentiment: {sentiment_result["label"]} (Confidence: {sentiment_result["score"]:.2f})')

        # Prevent the browser from closing
        while True:
            time.sleep(1)

    finally:
        # Close the browser
        driver.quit()

# Example usage
if __name__ == "__main__":
    keyword = "honey singh"
    result = get_video_titles(keyword)
    print(result)

