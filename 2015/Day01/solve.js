const fs = require('fs')

fs.readFile('input.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  part1(data)
  part2(data)
})

function part1(data) {
    console.log((data.match(/\(/g)).length - (data.match(/\)/g)).length)
}

function part2(data) {
    floor = 0
    for (let i = 0; i < data.length; i++) {
        (data[i] == '(')? floor++ : floor--;
        if (floor < 0) {
            console.log(i+1)
            break
        }
    }
}