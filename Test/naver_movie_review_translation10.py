from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

browser = webdriver.Chrome("../chromdriver/chromedriver.exe")
browser.maximize_window()

browser.get("https://papago.naver.com/")

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

movie_codes = movie_codes[900:1000]
movie_names = movie_names[900:1000]

sleep(5)

for cnt in range(len(movie_codes)):
  
  f = open("../reviews/naver_movie_review_" + str(cnt + 901) + "_" + movie_codes[cnt] + ".txt", 'r', encoding="UTF-8")

  reviews = f.read().split('\n')[1:-1]
  f.close()

  f = open("../translation/naver_movie_review_" + str(cnt + 901) + "_" + movie_codes[cnt] + ".txt", 'w', encoding="UTF-8")
  f.write(movie_names[cnt] + '\n')
  f.close()

  for i in range(len(reviews)):
    f = open("../translation/naver_movie_review_" + str(cnt + 901) + "_" + movie_codes[cnt] + ".txt", 'a', encoding="UTF-8")

    review = reviews[i].split(',')
    review[1] = ','.join(review[1:])
    review = review[:2]

    if review[1] == '':
      print('평점: ' + review[0])
      print('한글 리뷰: ' + review[1])
      print('영어 리뷰: ' + review[1])
      print()

      f.write(review[0] + ',')
      f.write(review[1] + '\n')

      f.close()
      continue

    browser.find_element_by_xpath("/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[3]/label").click()
    browser.find_element_by_xpath("/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[3]/label").send_keys(review[1])
    browser.find_element_by_xpath("/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[4]/div/button").click()
    
    sleep(5)

    soup = BeautifulSoup(browser.page_source, "lxml")
    result = soup.find("div", attrs={"id":"txtTarget"}).find("span").text

    print('평점: ' + review[0])
    print('한글 리뷰: ' + review[1])
    print('영어 리뷰: ' + result)
    print()

    f.write(review[0] + ',')
    f.write(result + '\n')

    browser.find_element_by_xpath("/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[3]/label/textarea").click()
    browser.find_element_by_xpath("/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[3]/label/textarea").clear()
  
    f.close()