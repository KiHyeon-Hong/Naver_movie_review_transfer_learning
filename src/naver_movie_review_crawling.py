import requests
from bs4 import BeautifulSoup
import re

p = re.compile('(\', \')')

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

f = open("../files/naver_movie_code.txt", 'r', encoding="UTF-8")

num = 0
movie_codes = []

while True:
  temp = f.readline().split('\n')[0]

  if temp == '':
    break

  if num % 2 == 1:
    movie_codes.append(temp)

  num = num + 1

f.close()

for cnt in range(len(movie_codes)):
  f = open("../reviews/naver_movie_review_" + movie_codes[cnt] + ".txt", 'w', encoding="UTF-8")

  url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=" + movie_codes[cnt] + "&target=after"
  res = requests.get(url, headers=headers)
  res.raise_for_status()

  soup = BeautifulSoup(res.text, "lxml")

  review_num = int(int(soup.find("strong", attrs={"class":re.compile("c_88 fs_11")}).text) / 10) + 1

  for num in range(1, review_num + 1):
    url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=" + movie_codes[cnt] + "&target=after&page=" + str(num)

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    reviews = soup.find("table", attrs={"class":re.compile("list_netizen")}).find("tbody").find_all("tr")

    for j in range(len(reviews)):
      data = reviews[j].find("td", attrs={"class":re.compile("title")})
      
      #  f.write(data.find("a", attrs={"class":re.compile("movie color_b")}).text + '\n')
      f.write(data.find('em').text + ',')

      temp = data.find("a", attrs={"class":re.compile("report")})['onclick']
      review = []

      while True:
        try:
          review.append(temp[:p.search(temp).span()[1]])
          temp = temp[p.search(temp).span()[1]:]
        except:
          break

      f.write(''.join(review[2:-1])[:-4] + '\n')

  f.close()