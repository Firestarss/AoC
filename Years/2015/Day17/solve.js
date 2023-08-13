const fs = require('fs')

fs.readFile('input.txt', 'utf8', (err, input) => {
    if (err) {
      console.error(err)
      return
    }
    data = input.split("\n")
    for (i = 0; i < data.length; i++) {
        data[i] = parseInt(data[i])
    }
    part1(powerSet(data))
    part2(powerSet(data))
  })
  
  function part1(data) {
    count = 0

    for (point of data) {
        sum = point.reduce((partial_sum, a) => partial_sum + a, 0);
        if (sum == 150) {
            count += 1
        }
    }
    console.log(count)
}

  function part2(data) {
    count = 0
    minContainers = 150

    for (point of data) {
        sum = point.reduce((partial_sum, a) => partial_sum + a, 0);
        if (sum == 150) {
            if (point.length < minContainers) {
                count = 0
                minContainers = point.length
            }
            if (point.length == minContainers) {
                count += 1
            }
        }
    }
    console.log(count)
}

const powerSet = 
      theArray => theArray.reduce(
        (subsets, value) => subsets.concat(
         subsets.map(set => [value,...set])
        ),
        [[]]
      );