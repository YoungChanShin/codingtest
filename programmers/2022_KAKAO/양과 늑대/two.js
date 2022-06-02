function solution(info, edges) {
  let answer = 0;
  let graph = Array.from({ length: info.length }, () => []);
  edges.forEach((edge) => graph[edge[0]].push(edge[1]));

  let dfs = (next, cur, sheep, wolf) => {
    sheep += info[cur] ^ 1;
    wolf += info[cur];
    answer = Math.max(sheep, answer);
    if (sheep <= wolf) {
      return;
    }

    const idx = next.indexOf(cur);
    if (idx > -1) {
      next.splice(idx, 1);
    }
    if (graph[cur].length) {
      graph[cur].forEach((node) => next.push(node));
    }
    next.forEach((node) => dfs([...next], node, sheep, wolf));
  };
  dfs([0], 0, 0, 0);
  return answer;
}
