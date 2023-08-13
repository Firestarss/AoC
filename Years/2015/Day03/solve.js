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
    const visited = new Set()
    coords = [0,0]
    visited.add(coords[0] + "," + coords[1])

    for (i=0; i<data.length; i++) {
        if (data[i] == "<") {coords = [coords[0] - 1, coords[1]]}
        if (data[i] == ">") {coords = [coords[0] + 1, coords[1]]}
        if (data[i] == "^") {coords = [coords[0], coords[1] + 1]}
        if (data[i] == "v") {coords = [coords[0], coords[1] - 1]}
        
        visited.add(coords[0] + "," + coords[1])
    }
    console.log(visited.size)
}

function part2(data) {
    const visited = new Set()
    s_coords = [0,0]
    r_coords = [0,0]
    visited.add(s_coords[0] + "," + s_coords[1])

    for (i=0; i<data.length; i++) {
        if (i % 2 == 1){
            if (data[i] == "<") {s_coords = [s_coords[0] - 1, s_coords[1]]}
            if (data[i] == ">") {s_coords = [s_coords[0] + 1, s_coords[1]]}
            if (data[i] == "^") {s_coords = [s_coords[0], s_coords[1] + 1]}
            if (data[i] == "v") {s_coords = [s_coords[0], s_coords[1] - 1]}

            visited.add(s_coords[0] + "," + s_coords[1])
        }
        else {
            if (data[i] == "<") {r_coords = [r_coords[0] - 1, r_coords[1]]}
            if (data[i] == ">") {r_coords = [r_coords[0] + 1, r_coords[1]]}
            if (data[i] == "^") {r_coords = [r_coords[0], r_coords[1] + 1]}
            if (data[i] == "v") {r_coords = [r_coords[0], r_coords[1] - 1]}

            visited.add(r_coords[0] + "," + r_coords[1])
        }
    }
    console.log(visited.size)
}