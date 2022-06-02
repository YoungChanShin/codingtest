const getSubset = () => {
  let res = [];
  const dfs = (start = 9, arr = []) => {
    res.push(arr);
    for (let i = start; i > -1; i--) {
      dfs(i - 1, [...arr, i]);
    }
  };

  dfs();
  return res;
};

function solution(n, info) {
  var answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  const cadidates = getSubset();
  //   const cadidates = [[0, 1]];
  let maxDiff = Number.MIN_SAFE_INTEGER;
  for (let wins of cadidates) {
    // 1. 화살 수 가능한지 확인
    const arrows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    let a = 0;
    for (let w of wins) {
      a += info[w] + 1; // 10-w 점 획득
      arrows[w] = info[w] + 1;
    }
    if (a > n) {
      continue;
    }
    // 2. 점수차 계산
    let score = 0;
    for (let i = 0; i < 11; i++) {
      if (wins.includes(i)) {
        score += 10 - i;
      } else if (info[i] !== 0) {
        score -= 10 - i;
      }
    }
    arrows[10] = n - arrows.reduce((a, b) => a + b, 0);
    if (0 < score && maxDiff < score) {
      maxDiff = score;
      answer = arrows;
    }
  }
  if (maxDiff === Number.MIN_SAFE_INTEGER) {
    answer = [-1];
  }
  return answer;
}

n = 5;
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0];

console.log(solution(n, info));
// console.log(3 in [1, 2, 3]);
