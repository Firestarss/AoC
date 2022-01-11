require 'digest'

md5 = Digest::MD5.new
done = false
counter = 0
key = "ckczppom"
match = "000000"

while done == false
    test_string = key + counter.to_s
    md5.reset
    hash = md5.update(test_string).hexdigest

    if hash[0..match.length-1] == match
        done = true
        puts counter
    end
    counter += 1
end