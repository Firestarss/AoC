# 232 (too low)

def is_nice_p1(test_string)
    vowel_count = test_string.scan(/[aeiou]/).length >= 3
    double_up = test_string.scan(/(.)\1/).length > 0
    no_blacklist = !(test_string =~ /ab|cd|pq|xy/i)

    return (vowel_count && double_up && no_blacklist)
end

def is_nice_p2(test_string)
    repeat = test_string =~ /(..).*\1/
    sandwich = test_string =~ /(.).\1/

    return (repeat && sandwich)
end

def part(num)
    count = 0
    File.readlines('input.txt').each do |line|
        if num == 1
            if is_nice_p1(line)
                count += 1
            end
        elsif num == 2
            if is_nice_p2(line)
                count += 1
            end
        end
    end
    puts count
end

part(1)
part(2)