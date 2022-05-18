const fs = require('fs');

const datas = fs
  .readFileSync(__dirname + '/../files/preprocessing_naver.txt', 'utf8')
  .split('\n')
  .map((v) => {
    v = v.split(',');
    return [parseInt(v[0]), v[1]];
  });

let neg = 0;
let pos = 0;

for (let i = 0; i < datas.length; i++) {
  let temp = datas[i][1];

  while (temp.length < 1000) temp += ' ' + datas[i][1];

  if (datas[i][0] < 7) {
    fs.writeFileSync(__dirname + `/../files/neg/${neg++}_${datas[i][0]}.txt`, temp, 'utf8');
  } else {
    fs.writeFileSync(__dirname + `/../files/pos/${pos++}_${datas[i][0]}.txt`, temp, 'utf8');
  }
}
