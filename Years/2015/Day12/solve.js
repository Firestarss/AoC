const fs = require('fs')

fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) {
      console.error(err)
      return
    }
    part1(data)
    part2(data)
  })

  function recurse(data) {
    // base cases
    if (data.constructor.name === "Number") {
        return data
    }
    else if (data.constructor.name === "Object" && Object.values(data).includes("red")) {
        return 0
    }

    // recursive case
    if (data.constructor.name === "Object") {
        data = Object.values(data)
    }
    if (data.constructor.name === "Array") {
        if (data.length === 1) {
            return recurse(data[0])
        }
        return data.reduce((a, b) => recurse(a) + recurse(b))
    }

    return 0
  }

  function part1(data) {
      total = 0
      const numbers = data.match(/-*\d+/g)

      for (const number of numbers) {
          total += number * 1
      }
      console.log(total)
  }

  function part2(data) {
      input = JSON.parse(data)
      console.log(recurse(input))
  }