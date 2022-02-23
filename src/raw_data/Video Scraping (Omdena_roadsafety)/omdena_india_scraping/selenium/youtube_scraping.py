# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os, time
#
# #youtube links
# links_path='../spiders/reddit_roadcam.txt'
# file=open(links_path, 'r')
# links=[x[:-1] for x in file.readlines() if 'youtu.be' in x or 'youtube' in x]
#
#
#
# #launch site
# chromeOptions = webdriver.ChromeOptions()
# prefs = {"download.default_directory" : r"C:\Users\ASUS\Desktop\Omdena_Scraping\omdena_india_scraping\omdena_india_scraping\selenium\Vids"}
# chromeOptions.add_experimental_option("prefs",prefs)
# PATH='C:\Program Files (x86)\chromedriver.exe'
# driver=webdriver.Chrome(PATH, options=chromeOptions)
# #driver.get('https://en.savefrom.net/75/')
#
# #vid counter
# vid_counter=0
# numVids_add_on=0 #increment numVids even when not succesfully DLed, to keep track of queue
#
# for link in links:
#     driver.get('https://en.savefrom.net/75/')
#     #enter youtube url and submit
#     search=driver.find_element_by_name('sf_url')
#     search.send_keys(link)
#     search=driver.find_element_by_name('sf_submit')
#     search.send_keys(Keys.RETURN)
#
#
#
#     #download
#     try:
#         dl_link = WebDriverWait(driver, 35).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "div.def-btn-box a"))
#         )
#
#         driver.get(dl_link.get_attribute('href'))
#     except:
#         numVids_add_on+=1
#
#     #queue
#     numVids=len(os.listdir('Vids')) #count videos to initiate new download when previous finished
#     numVids+=numVids_add_on #increment by non succesfully DLed vids to maintain queue
#     while numVids<=vid_counter:
#         time.sleep(3)
#         numVids = len(os.listdir('Vids'))
#     vid_counter+=1
#
#
#
# driver.quit()



from pytube import YouTube

links_path='../spiders/reddit_roadcam.txt'
file=open(links_path, 'r')
links=[x[:-1] for x in file.readlines() if 'youtu.be' in x or 'youtube' in x]
links=links[500:]


SAVE_PATH=r"C:\Users\ASUS\Desktop\Omdena_Scraping\omdena_india_scraping\omdena_india_scraping\selenium\Vids"

for link in links:
    try:
        yt=YouTube(link)
        length=yt.length

        if length<250:
            # filters out all the files with "mp4" extension
            mp4files = yt.streams.filter(file_extension='mp4')

            # get the video with the extension and
            # resolution passed in the get() function
            d_video = mp4files[0]

            # download
            d_video.download(SAVE_PATH)

    except:
        pass