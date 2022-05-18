const fs = require('fs');

const korean = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;

const datas = fs
  .readFileSync(__dirname + '/../files/naver.txt', 'utf8')
  .split('\n')
  .map((v) => {
    return v.split('\r')[0];
  })
  .map((v) => {
    return v.split(',');
  })
  .filter((v) => {
    return v.length === 2;
  })
  .filter((v) => {
    return v[1] !== '';
  })
  .filter((v) => {
    return !korean.test(v[1]);
  });

let data = '';

for (let i = 0; i < datas.length; i++) {
  data += datas[i][0] + ',' + datas[i][1] + '\n';
}

fs.writeFileSync(__dirname + '/../files/preprocessing_naver.txt', data, 'utf8');
