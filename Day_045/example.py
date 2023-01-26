import requests
from bs4 import BeautifulSoup
url = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(url.text, 'html.parser')
mov_title = soup.findAll(name="h3", class_="title")
# titles = []
# for title in mov_title:
#     titles.append(title.getText())
titles = [movie.getText() for movie in mov_title]
titles = titles[::-1]
with open("Day_045/movie100.txt", "w") as write_mv:
    for movie in titles:
        # for movie in range(len(titles)-1, -1, -1):
        #     write_mv.write(titles[movie])
        write_mv.write(movie)
        write_mv.write("\n")
