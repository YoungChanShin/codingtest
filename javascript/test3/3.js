function solution(next_student) {
    var answer = 0;
    const numOfStudent = next_student.length

    const studentsMatrix = new Array(numOfStudent);
    const cnt = [0] * numOfStudent

    for (let i = 0; i < numOfStudent; i++) {
        studentsMatrix[i] = [];
    }
    for (let i = 0; i < numOfStudent; i++) {
        let next_student_idx = next_student[i] - 1
        while (!studentsMatrix[i].includes(next_student_idx) && next_student_idx > -1 && next_student_idx !== i) {
            studentsMatrix[i].push(next_student_idx)
            next_student_idx = next_student[next_student_idx] - 1
            if (cnt[next_student_idx] !== 0) {
                studentsMatrix[i].push(...studentsMatrix[next_student_idx])
                break
            }
        }
        cnt[i] = studentsMatrix[i].length + 1
    }

    for (let i = 0; i < numOfStudent; i++) {
        studentsMatrix[i] = studentsMatrix[i].length + 1
    }
    return indexOfMax(studentsMatrix) + 1;
}

function indexOfMax(arr) {
    if (arr.length === 0) {
        return -1;
    }
    const len = arr.length

    let max = arr[len - 1];
    let maxIndex = len - 1;

    for (let i = maxIndex; i > -1; i--) {
        if (arr[i] > max) {
            maxIndex = i;
            max = arr[i];
        }
    }

    return maxIndex;
}

// function recur(studentId, memo, next_student) {
//     if (memo[studentId] !== 0) {

//         return memo[studentId] + 1
//     }else {
//         return memo[studentId]
//     }
// }


// const next_student = [5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]
const next_student = [6, 10, 8, 5, 8, 10, 5, 1, 6, 7]

console.log(solution(next_student))