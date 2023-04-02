function solution(board) {
  const N = board.length;
  const visited = Array.from(Array(N), () => Array(N).fill([0, 0]));
  const valid = (r, c, N) => 0 <= r && r < N && 0 <= c && c < N;
  const q = [];
  q.push([0, 0, 0]);
  while (q.length > 0) {
    let [r, c, p] = q.shift();
    let t = visited[r][c][p];

    // 가로로 누워있는 상태
    if (p === 0) {
      // 종료조건
      if (r === N - 1 && c + 1 === N - 1) {
        return t;
      }
      // 위쪽으로
      if (
        valid(r - 1, c, N) &&
        valid(r - 1, c + 1, N) &&
        board[r - 1][c] === 0 &&
        board[r - 1][c + 1] === 0
      ) {
        // 1. 반시계 방향
        if (visited[r - 1][c][1] === 0) {
          visited[r - 1][c][1] = t + 1;
          q.push([r - 1, c, 1]);
        }
        // 2. 시계 방향
        if (visited[r - 1][c + 1][1] === 0) {
          visited[r - 1][c + 1][1] = t + 1;
          q.push([r - 1, c + 1, 1]);
        }
        // 3. 평행이동
        if (visited[r - 1][c][0] === 0) {
          visited[r - 1][c][0] = t + 1;
          q.push([r - 1, c, 0]);
        }
        // 아래로
      }
      if (
        valid(r + 1, c, N) &&
        valid(r + 1, c + 1, N) &&
        board[r + 1][c] === 0 &&
        board[r + 1][c + 1] === 0
      ) {
        // 4. 시계방향
        if (visited[r][c][1] === 0) {
          visited[r][c][1] = t + 1;
          q.push([r, c, 1]);
        }
        // 5. 반시계방향
        if (visited[r][c + 1][1] === 0) {
          visited[r][c + 1][1] = t + 1;
          q.push([r, c + 1, 1]);
        }
        // 6. 평행이동
        if (visited[r + 1][c][0] === 0) {
          visited[r + 1][c][0] = t + 1;
          q.push([r + 1, c, 0]);
        }
      }
      // 7. 왼쪽으로
      if (valid(r, c - 1, N) && board[r][c - 1] === 0) {
        if (visited[r][c - 1][0] === 0) {
          visited[r][c - 1][0] = t + 1;
          q.push([r, c - 1, 0]);
        }
      }
      // 8. 오른쪽으로
      if (valid(r, c + 2, N) && board[r][c + 2] === 0) {
        if (visited[r][c + 1][0] === 0) {
          visited[r][c + 1][0] = t + 1;
          q.push([r, c + 1, 0]);
        }
      }

      // 세로로 서있는 상태
    } else {
      if (r + 1 === N - 1 && c === N - 1) {
        return t;
      }
      // 오른쪽으로
      if (
        valid(r, c + 1, N) &&
        valid(r + 1, c + 1, N) &&
        board[r][c + 1] === 0 &&
        board[r + 1][c + 1] === 0
      ) {
        // 1. 반시계방향
        if (visited[r][c][0] === 0) {
          visited[r][c][0] = t + 1;
          q.push([r, c, 0]);
        }
        // 2. 시계방향
        if (visited[r + 1][c][0] === 0) {
          visited[r + 1][c][0] = t + 1;
          q.push([r + 1][c][0]);
        }
        // 3. 평행이동
        if (visited[r][c + 1][1] === 0) {
          visited[r][c + 1][1] = t + 1;
          q.push([r, c + 1, 1]);
        }
      }
      // 왼쪽으로
      if (
        valid(r, c - 1, N) &&
        valid(r + 1, c - 1, N) &&
        board[r][c - 1] === 0 &&
        board[r + 1][c - 1] === 0
      ) {
        // 4. 시계방향
        if (visited[r][c - 1][0] === 0) {
          visited[r][c - 1][0] = t + 1;
          q.push([r, c - 1, 0]);
        }
        // 5. 반시계방향
        if (visited[r + 1][c - 1][0] === 0) {
          visited[r + 1][c - 1][0] = t + 1;
          q.push([r + 1, c - 1, 0]);
        }
        // 6. 평행이동
        if (visited[r][c - 1][0] === 0) {
          visited[r][c - 1][0] = t + 1;
          q.push([r, c - 1, 0]);
        }
      }
      // 7. 위로
      if (valid(r - 1, c, N) && board[r - 1][c] === 0) {
        if (visited[r - 1][c][1] === 0) {
          visited[r - 1][c][1] = t + 1;
          q.push([r - 1, c, 1]);
        }
      }

      // 8. 아래로
      if (valid(r + 2, c, N) && board[r + 2][c] === 0) {
        if (visited[r + 1][c][1] === 0) {
          visited[r + 1][c][1] = t + 1;
          q.push([r + 1, c, 1]);
        }
      }
    }
  }

  console.log(visited);

  return 0;
}

const board = [
  [0, 0, 0, 1, 1],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 1, 1],
  [1, 1, 0, 0, 1],
  [0, 0, 0, 0, 0],
];
console.log(solution(board));
