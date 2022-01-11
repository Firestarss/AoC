require 'digest'

$md5 = Digest::MD5.new
key = "ckczppom"

def match_hash(key, match)
    done = false
    counter = 0
    while done == false
        test_string = key + counter.to_s
        $md5.reset
        hash = $md5.update(test_string).hexdigest

        if hash[0..match.length-1] == match
            done = true
            puts counter
        end
        counter += 1
    end
end

match_hash(key, "00000")
match_hash(key, "000000")