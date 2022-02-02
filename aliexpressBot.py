from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def ctor():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    return driver

def dtor(driver):
    driver.quit()

def getLinksAliexpress(keywords, driver):
    links = []
    for i in keywords:
        driver.get(("https://www.aliexpress.com/wholesale?SearchText={}").format(i))
        time.sleep(0.5)
        y = 100
        for j in range(30):
            driver.execute_script("window.scrollTo(0, {})".format(y))
            y += 200
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for item in soup.find_all("a", class_="_3t7zg _2f4Ho"):
            links.append(item["href"])
    return links

def getKeywords():
    keywords = []
    file = open("input.txt", "r")
    for i in file.readlines():
        keywords.append(i.replace("\n", ""))
    return keywords

def main():
    keywords = getKeywords()
    driver = ctor()
    links = getLinksAliexpress(keywords, driver)

    dtor(driver)

if __name__ == '__main__':
    main()