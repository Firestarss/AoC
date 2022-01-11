const fs = require('fs')

fs.readFile('input.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  const input = data.split("\n")
  part1(input)
  part2(input)
})

function part1(data) {
    output = 0
    for (const point of data) {
        const lwh = point.split("x")
        const sides = [lwh[0] * lwh[1], lwh[1] * lwh[2], lwh[2] * lwh[0]]
        const sum = sides.reduce((partial_sum, a) => partial_sum + a)
        const min_side = sides.reduce((a,b) => a < b? a:b)
        output += sum * 2 + min_side
    }
    console.log(output)
}

function part2(data) {
    output = 0
    for (const point of data) {
        const lwh = point.split("x")
        const sides = [lwh[0]*1 + lwh[1]*1, lwh[1]*1 + lwh[2]*1, lwh[2]*1 + lwh[0]*1]
        const vol = lwh.reduce((a,b) => a*b)
        const min_side = sides.reduce((a,b) => a < b? a:b)
        output += min_side * 2 + vol
    }
    console.log(output)
}