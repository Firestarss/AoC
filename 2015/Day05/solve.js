const fs = require('fs')

fs.readFile('input.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  input = data.split("\n")
  console.log(input.filter(part1).length)
  console.log(input.filter(part2).length)
})

function part1(data) {
    const vowels = data.match(/[aeiou]/g) || []
    const double = data.match(/(.)\1/)
    const illegal = data.match(/ab|cd|pq|xy/)

    return (vowels.length > 2 && double && !illegal)
}

function part2(data) {
    repeat = data.match(/(..).*\1/)
    sandwich = data.match(/(.).\1/)

    return (repeat && sandwich)
}