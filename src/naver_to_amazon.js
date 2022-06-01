const fs = require('fs');

const datas = fs
  .readFileSync(__dirname + '/../files/preprocessing_naver.txt', 'utf8')
  .split('\n')
  .map((v) => {
    v = v.split(',');
    return [parseInt(v[0]), v[1]];
  });

fs.writeFileSync(__dirname + '/../files/amazonTemplate.txt', '', 'utf8');
fs.writeFileSync(__dirname + '/../files/amazonTemplate_pos.txt', '', 'utf8');
fs.writeFileSync(__dirname + '/../files/amazonTemplate_neg.txt', '', 'utf8');

for (let i = 0; i < datas.length; i++) {
  let temp = '';

  if (datas[i][0] < 7) {
    temp += '__label__1 ';
  } else {
    temp += '__label__2 ';
  }

  temp += datas[i][1] + ': ' + datas[i][1];

  while (temp.length < 100) temp += ' ' + datas[i][1];

  fs.appendFileSync(__dirname + '/../files/amazonTemplate.txt', temp + '\n', 'utf8');

  if (datas[i][0] < 7) {
    fs.appendFileSync(__dirname + '/../files/amazonTemplate_neg.txt', temp + '\n', 'utf8');
  } else {
    fs.appendFileSync(__dirname + '/../files/amazonTemplate_pos.txt', temp + '\n', 'utf8');
  }
}
