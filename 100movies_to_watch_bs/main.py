import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.raise_for_status()
website= response.text

soup = BeautifulSoup(website, "html.parser")
movies_links = soup.find_all(name="h3", class_="title")
movies = [movie.text for movie in movies_links]
with open("movies.txt", mode="w") as file:
    for movie in reversed(movies):
        try:
            file.write(f"{movie.split(')')[0]}:{movie.split(')')[1]} \n")
        except IndexError:
            file.write(movie)
        except UnicodeEncodeError:
            name = f"{movie.split(')')[0]}:{movie.split(')')[1]}".encode('utf8')
            file.write(f"{name} \n")