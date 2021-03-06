import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

f = open("../files/naver_movie_code.txt", 'r', encoding="UTF-8")

num = 0
movie_codes = []
movie_names = []

while True:
  temp = f.readline().split('\n')[0]

  if temp == '':
    break

  if num % 2 == 1:
    movie_codes.append(temp)
  else:
    movie_names.append(temp)

  num = num + 1

f.close()

for cnt in range(len(movie_codes)):
  print(movie_names[cnt] + '   ' + movie_codes[cnt])

  f = open("../reviews/naver_movie_review_" + str(cnt + 1) + "_" + movie_codes[cnt] + ".txt", 'w', encoding="UTF-8")

  url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=" + movie_codes[cnt] + "&target=after"
  res = requests.get(url, headers=headers)
  res.raise_for_status()

  soup = BeautifulSoup(res.text, "lxml")

  review_num = int(int(soup.find("strong", attrs={"class":re.compile("c_88 fs_11")}).text) / 10) + 1

  if review_num > 1000:
    review_num = 1000

  f.write(movie_names[cnt] + '\n')

  for num in range(1, review_num + 1):
    url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=" + movie_codes[cnt] + "&target=after&page=" + str(num)

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    reviews = soup.find("table", attrs={"class":re.compile("list_netizen")}).find("tbody").find_all("tr")

    for j in range(len(reviews)):
      try:
        data = reviews[j].find("td", attrs={"class":re.compile("title")})

        f.write(data.find('em').text + ',')
        f.write(reviews[j].text.split('\n')[7].strip() + '\n')
      except:
        continue

  f.close()