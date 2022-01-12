def step(input)
    sequences = input.scan(/((\d)\2*)/)
    temp = ""

    sequences.each { |sequence| temp << sequence[0].length.to_s << sequence[1]}

    temp
end
    
def part1(input)
    40.times { input = step(input)}
    input.length
end

def part2(input)
    50.times { input = step(input)}
    input.length
end

input = 1113222113.to_s

p part1(input)
p part2(input)