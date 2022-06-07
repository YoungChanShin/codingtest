const pre = [];
const post = [];

function solution(nodeinfo) {
  class Tree {
    constructor(value = -1, idx = -1) {
      this.val = value;
      this.num = idx;
      this.left = null;
      this.right = null;
    }
    insert = (value, idx) => {
      if (this.val === -1) {
        this.val = value;
        this.num = idx;
        return;
      } else {
        if (value < this.val) {
          if (this.left === null) {
            this.left = new Tree(value, idx);
          } else {
            this.left.insert(value, idx);
          }
        } else {
          if (this.right === null) {
            this.right = new Tree(value, idx);
          } else {
            this.right.insert(value, idx);
          }
        }
      }
    };

    preOrder = () => {
      pre.push(this.num);
      if (this.left !== null) {
        this.left.preOrder();
      }
      if (this.right !== null) {
        this.right.preOrder();
      }
    };

    postOrder = () => {
      if (this.left !== null) {
        this.left.postOrder();
      }
      if (this.right !== null) {
        this.right.postOrder();
      }
      post.push(this.num);
    };
  }

  nodeinfo.map((el, idx) => el.push(idx + 1));

  nodeinfo.sort((a, b) => {
    let diff = b[1] - a[1];
    if (diff === 0) {
      diff = a[0] - b[0];
    }
    return diff;
  });

  const binaryTree = new Tree();
  nodeinfo.forEach((el) => {
    binaryTree.insert(el[0], el[2]);
  });
  binaryTree.preOrder();
  binaryTree.postOrder();
  return [pre, post];
}

const nodeinfo = [
  [5, 3],
  [11, 5],
  [13, 3],
  [3, 5],
  [6, 1],
  [1, 3],
  [8, 6],
  [7, 2],
  [2, 2],
];

console.log(solution(nodeinfo));
