import googletrans

translator = googletrans.Translator()

f = open("./files/naver_movie_code.txt", 'r', encoding="UTF-8")

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

movie_codes = movie_codes[1200:1400]
movie_names = movie_names[1200:1400]


for cnt in range(len(movie_codes)):
  f = open("./reviews/naver_movie_review_" + str(cnt + 1201) + "_" + movie_codes[cnt] + ".txt", 'r', encoding="UTF-8")

  reviews = f.read().split('\n')[1:-1]
  f.close()

  f = open("./translation/naver_movie_review_" + str(cnt + 1201) + "_" + movie_codes[cnt] + ".txt", 'w', encoding="UTF-8")
  f.write(movie_names[cnt] + '\n')
  f.close()

  for i in range(len(reviews)):
    f = open("./translation/naver_movie_review_" + str(cnt + 1201) + "_" + movie_codes[cnt] + ".txt", 'a', encoding="UTF-8")

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

    result = translator.translate(review[1], src='ko', dest='en')

    print('평점: ' + review[0])
    print('한글 리뷰: ' + review[1])
    print('영어 리뷰: ' + result.text)
    print()

    f.write(review[0] + ',')
    f.write(result.text + '\n')
  
    f.close()