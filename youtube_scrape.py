from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Edge(executable_path='edgedriver\MicrosoftWebDriver.exe')

url = "https://www.youtube.com/@JohnWatsonRooney/videos"

driver.get(url)

# Pulled in elements below, found highest level for container, then used inspect -> copy -> XPath for the elements.
# "style-scope ytd-rich-grid-media"

# //*[@id="video-title"]
# //*[@id="metadata-line"]/span[1]
# //*[@id="metadata-line"]/span[2]

videos = driver.find_elements_by_class_name('style-scope ytd-rich-grid-media')

video_list = []

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
 
    vid_item = {
        'title': title,
        'views': views,
        'posted': when
    }
    video_list.append(vid_item)

df = pd.DataFrame(video_list)

print(df)

df.to_csv('video_list.csv')