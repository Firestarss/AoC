const fs = require('fs')

fs.readFile('input.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1}

  part1(data, ticker_tape)
  part2(data, ticker_tape)
})

function part1(data, ticker_tape) {
    data = data.split("\n")

    for (i = 0; i < data.length; i++) {
        local_list = data[i].split(" ").slice(2)
        is_aunt = true
        for (j = 0; j < local_list.length; j+=2) {
            key = local_list[j].substring(0,local_list[j].length - 1)
            value = local_list[j+1]

            if (value[value.length-1] == ",") {
                value = value.substring(0,value.length - 1)
            }

            value = parseInt(value)

            if (ticker_tape[key] != value) {
                is_aunt = false
            }
        }
        if (is_aunt) {
            console.log(i + 1)
        }
    }
}

function part2(data, ticker_tape) {
    data = data.split("\n")

    for (i = 0; i < data.length; i++) {
        local_list = data[i].split(" ").slice(2)
        is_aunt = true
        for (j = 0; j < local_list.length; j+=2) {
            key = local_list[j].substring(0,local_list[j].length - 1)
            value = local_list[j+1]

            if (value[value.length-1] == ",") {
                value = value.substring(0,value.length - 1)
            }

            value = parseInt(value)

            if (key == "cats" || key == "trees") {
                if (ticker_tape[key] >= value) {
                    is_aunt = false
                }
            }
            else if (key == "pomeranians" || key == "goldfish") {
                if (ticker_tape[key] <= value) {
                    is_aunt = false
                }
            }
            else if (ticker_tape[key] != value) {
                is_aunt = false
            }
        }
        if (is_aunt) {
            console.log(i + 1)
        }
    }
}