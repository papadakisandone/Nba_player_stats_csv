import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd


options = Options()
options.add_argument("start-maximized")
s = Service(r'C:\Users\jojob\.wdm\drivers\chromedriver\win32\98.0.4758.102\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
url = "https://www.nba.com/"

driver.get(url)  # open a new tab in the new window
time.sleep(2)
# when the element is visible, cklick it
wait = WebDriverWait(driver, 10)
players = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='nav-ul']/li[10]/a/span[1]")))
players.click()

search_player = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[3]/section/div/div[1]/div/input')))
search_player.send_keys("antetokounmpo")
search_player.send_keys(Keys.ENTER)
time.sleep(2)
giannis = wait.until((EC.visibility_of_element_located((By.XPATH,
                                                        "//*[@id='__next']/div[2]/div[3]/section/div/div[2]/div["
                                                        "2]/div/div/div/table/tbody/tr[1]/td[1]/a/div[2]/p[1]"))))
giannis.click()
time.sleep(2)

# get data from the table
table = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='__next']/div[2]/div[5]/section[2]/div/div/div/table"))).get_attribute('outerHTML')

soup = BeautifulSoup(table, 'html.parser')
df_table = pd.read_html(str(soup))[0]

df_table.to_csv('last_5_games_stats.csv')
