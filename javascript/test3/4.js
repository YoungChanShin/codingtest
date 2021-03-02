function solution(m, v) {
    const ma = new Array(v.length);
    for (let i = 0; i < v.length; i++) {
        ma[i] = m;
    }
    console.log(ma)
    let lowest = 0
    for (let i = 0; i < v.length; i++) {
        for (let j = i; j > -1; j--) {
            if (lowest === j) {
                lowest += 1
            }
        }
    }
    return lowest
}

m = 4
v = [2, 3, 1]

solution(m, v)