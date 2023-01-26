from bs4 import BeautifulSoup
import requests
## import lxml
# lxml parser
with open("Day_045/website.html") as readHtml:
    contents = readHtml.read()
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)  # name of title tag
print(soup.prettify())
print(soup.a)  # first a
all_a_tag = soup.find_all(name="a")
print(all_a_tag)  # all a
for tag in all_a_tag:
    print(tag.getText())  # only text
    print(tag.get("href"))  # only href

heading = soup.find(name="h1", id="name")  # search id
print(heading)
section_heading = soup.find(name="h3", class_="heading")  # search class
print(section_heading.getText())
# like css selector it can select #id or .class
company_url = soup.select_one(selector="p a")
print(company_url)
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(class_="titleline")
article_links = []
article_texts = []
for article in articles:
    article_text = article.a.getText()
    article_texts.append(article_text)
    article_link = article.a.get("href")
    article_links.append(article_link)


article_upvote = [int(score.getText().split()[0])
                  for score in soup.find_all(class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)

max_upvote = max(article_upvote)
max_index = article_upvote.index(max_upvote)
print(max_upvote)
print(article_texts[max_index])
print(article_links[max_index])
