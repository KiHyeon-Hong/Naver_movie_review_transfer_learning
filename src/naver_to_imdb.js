const fs = require('fs');

const datas = fs
  .readFileSync(__dirname + '/../files/preprocessing_naver.txt', 'utf8')
  .split('\n')
  .map((v) => {
    v = v.split(',');
    return [parseInt(v[0]), v[1]];
  });

let neg_train = 0;
let pos_train = 0;
let neg_test = 0;
let pos_test = 0;

for (let i = 0; i < datas.length; i++) {
  let temp = datas[i][1];

  while (temp.length < 1000) temp += ' ' + datas[i][1];

  if (datas[i][0] < 7) {
    if (neg_test < 10000) {
      fs.writeFileSync(__dirname + `/../files/neg_test/${neg_test++}_${datas[i][0]}.txt`, temp, 'utf8');
    } else {
      fs.writeFileSync(__dirname + `/../files/neg_train/${neg_train++}_${datas[i][0]}.txt`, temp, 'utf8');
    }
  } else {
    if (pos_test < 10000) {
      fs.writeFileSync(__dirname + `/../files/pos_test/${pos_test++}_${datas[i][0]}.txt`, temp, 'utf8');
    } else {
      fs.writeFileSync(__dirname + `/../files/pos_train/${pos_train++}_${datas[i][0]}.txt`, temp, 'utf8');
    }
  }
}
