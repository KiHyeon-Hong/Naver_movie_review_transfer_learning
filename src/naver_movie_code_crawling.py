import requests
from bs4 import BeautifulSoup
import re

date = 20220415

f = open("../files/naver_movie_code.txt", 'w', encoding="UTF-8")

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

for i in range(40):
  url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=" + str(date) + "&page=" + str(i)
  res = requests.get(url, headers=headers)
  res.raise_for_status()

  soup = BeautifulSoup(res.text, "lxml")

  movies = soup.find("table", attrs={"class":re.compile("list_ranking")}).find("tbody").find_all("tr")

  for j in range(len(movies)):
    data = movies[j].find("div", attrs={"class":re.compile("tit5")})

    if data:
      f.write(data.find('a').text + '\n')
      f.write(data.find('a')['href'].split('=')[-1] + '\n')