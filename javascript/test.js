let a = [{ f1: 1, f2: 2 }, { f1: 3, f2: 4 }]
const idx = a.findIndex(function (item) { return item.f1 === 1 }) // findIndex = find + indexOf if (idx > -1) a.splice(idx, 1)
console.log(idx)