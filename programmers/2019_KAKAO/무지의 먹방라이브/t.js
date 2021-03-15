// function foo(b) {
//     const a = '1'
//     callback1 = (b) => {
//         console.log(a)
//         console.log(b)
//     }
//     callback1(b)
// }

// foo('2')
function foo() {
    new Promise(function (resolve, reject) {
        setTimeout(() => resolve(a), 100); // (*)
    }).then(function (result) { // (**)
        console.log(result); // 1
        return result * 2;
    });
}

function boo(event) {
    foo();
}

const a = 1;
boo(a);