from bs4 import BeautifulSoup
import requests


url = "https://realpython.github.io/fake-jobs/"
#input("Enter the full URl of the website you want to scrape.")

#wntd = input("What are you searching for on the page?")

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

b = soup.find_all("h3", "title is-6 company")

a = soup.find_all("h2", "title is-5")


for i in a:
    for b in i:
        print(i.string)
        print(b.string)


