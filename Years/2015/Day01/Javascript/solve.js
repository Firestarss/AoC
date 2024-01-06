const fs = require('fs');

function part1(data) {
    const countOpen = data.split('(').length - 1;
    const countClose = data.split(')').length - 1;
    console.log(countOpen - countClose);
}

function part2(data) {
    let floor = 0;
    for (let i = 0; i < data.length; i++) {
        const char = data.charAt(i);
        floor = char === '(' ? floor + 1 : floor - 1;
        if (floor < 0) {
            console.log(i + 1);
            break;
        }
    }
}

const data = fs.readFileSync('../input.txt', 'utf8');
part1(data);
part2(data);
