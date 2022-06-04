const copy_board = Array.from(Array(5), () => Array(5).fill(0));
const visited = Array.from(Array(5), () => Array(5).fill(0));
let [N, M] = [0, 0];
const dr = [0, 0, 1, -1];
const dc = [1, -1, 0, 0];

const valid = (r, c) => r < 0 || c < 0 || r >= N || c >= M;

const solve = (myr, myc, opr, opc) => {
  if (visited[myr][myc] == 1) return 0;
  let ret = 0;
  for (let i = 0; i < 4; i++) {
    let new_r = myr + dr[i];
    let new_c = myc + dc[i];

    if (
      valid(new_r, new_c) ||
      visited[new_r][new_c] == 1 ||
      copy_board[new_r][new_c] == 0
    )
      continue;

    visited[myr][myc] = 1;
    let val = solve(opr, opc, new_r, new_c) + 1;
    visited[myr][myc] = 0;

    if (val % 2 && ret % 2) ret = Math.min(ret, val);
    else if (val % 2 && ret % 2 == 0) ret = val;
    else if (val % 2 == 0 && ret % 2 == 0) ret = Math.max(ret, val);
  }

  return ret;
};
function solution(board, aloc, bloc) {
  N = board.length;
  M = board[0].length;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      copy_board[i][j] = board[i][j];
    }
  }

  return solve(...aloc, ...bloc);
}

const board = [
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1],
];
aloc = [1, 0];
bloc = [1, 2];

console.log(solution(board, aloc, bloc));
