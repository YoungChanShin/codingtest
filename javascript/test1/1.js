
function solution(n, record) {
    const serversAndNickname = new Array(n);

    for (let i = 0; i < n; i++) {
        serversAndNickname[i] = new Array();
    }

    numOfUsers = record.length
    for (let i = 0; i < numOfUsers; i++) {
        const userInfo = record[i].split(' ')
        const server = Number(userInfo[0]) - 1
        const nickname = userInfo[1]
        // 중복 확인
        let flag = false
        let NumOfServerUsers = serversAndNickname[server].length
        for (let j = 0; j < NumOfServerUsers; j++) {
            if (serversAndNickname[server][j] === nickname) {
                // 삽입 없이 종료
                flag = true
                break
            }
        }
        if (flag === true) {
            continue
        }
        // 5인 이상인 경우 오래된 유저 삭제
        if (NumOfServerUsers >= 5) {
            serversAndNickname[server].shift()
        }

        // 삽입
        serversAndNickname[server].push(nickname)


    }
    const answer = []
    for (let i = 0; i < n; i++) {
        let NumOfServerUsers = serversAndNickname[i].length
        for (let j = 0; j < NumOfServerUsers; j++) {
            answer.push(serversAndNickname[i][j])
        }
    }
    return answer;
}
// const n = 1
// const record = ["1 fracta", "1 sina", "1 hana", "1 robel", "1 abc", "1 sina", "1 lynn"]

const n = 4
const record = ["1 a", "1 b", "1 abc", "3 b", "3 a", "1 abcd", "1 abc", "1 aaa", "1 a", "1 z", "1 q", "3 k", "3 q", "3 z", "3 m", "3 b"]
console.log(solution(n, record))