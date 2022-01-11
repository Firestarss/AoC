var crypto = require('crypto');

function match_hash(key, match) {
    counter = 0
    while (true){
        test = key + counter
        hash = crypto.createHash('md5').update(test).digest('hex');

        if (hash.substring(0, match.length) == match){
            console.log(counter)
            break
        }
        counter++
    }
}

key = "ckczppom"
match_hash(key, "00000")
match_hash(key, "000000")