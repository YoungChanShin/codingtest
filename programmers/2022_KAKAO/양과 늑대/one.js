function solution(info, edges) {
  var answer = 1;
  const dfs = (
    start = 0,
    state = { sheepes: 1, wolves: 0 },
    cadidates = []
  ) => {
    cadidates = [
      ...cadidates,
      ...edges.filter((e) => e[0] === start).map((e) => e[1]),
    ];

    for (let nextidx in cadidates) {
      let next = cadidates[nextidx];
      let newCandidates = [...cadidates];
      newCandidates.splice(nextidx, 1);

      if (info[next] === 0) {
        answer = Math.max(answer, state.sheepes + 1);
        dfs(next, { ...state, sheepes: state.sheepes + 1 }, newCandidates);
      } else if (state.sheepes > state.wolves + 1) {
        dfs(next, { ...state, wolves: state.wolves + 1 }, newCandidates);
      }
    }
  };

  dfs();
  return answer;
}

const info = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
const edges = [
  [0, 1],
  [1, 2],
  [1, 4],
  [0, 8],
  [8, 7],
  [9, 10],
  [9, 11],
  [4, 3],
  [6, 5],
  [4, 6],
  [8, 9],
];

console.log(solution(info, edges));
