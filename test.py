# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# # Setup the Chrome driver
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)

# # Open YouTube
# driver.get("https://www.youtube.com/")

# # Find the search box and input the keyword
# keyword = input('Song')
# search_box = driver.find_element("name", "search_query")
# search_box.send_keys(keyword)
# search_box.submit()

# # Wait for the search results to load
# time.sleep(5)

# # Find and print the titles of the top 10 videos
# video_titles = driver.find_elements(by='id', value= "video-title")
# for i, title in enumerate(video_titles[:10], 1):
#     print(f"{i}. {title.get_attribute('title')}")

# # Close the browser
# driver.quit()
