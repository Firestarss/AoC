require 'set'

def eval_dist(seats)
    total = 0
    for i in (0..seats.length-2)
        total += $happiness[[seats[i], seats[i+1]]]
        total += $happiness[[seats[i+1], seats[i]]]
    end
    total += $happiness[[seats[0], seats[-1]]]
    total += $happiness[[seats[-1], seats[0]]]
    return total
end

def part1()
    p Array(Array($people).permutation($people.length)).map { |seats| eval_dist(seats)}.max
end

def part2()
    for person in $people
        $happiness[[person, "me"]] = 0
        $happiness[["me", person]] = 0
    end
    $people.add("me")
    part1()
end
    
lines = File.readlines('input.txt')

$people = Set.new
$happiness = Hash.new

for line in lines
    local_people = line.scan(/[a-zA-Z]+/)
    $people = $people | [local_people[0], local_people[-1]]

    gain_lose = line.match(/gain|lose/)[0]
    value = line.match(/\d+/)[0].to_i

    if gain_lose == "lose"
        value *= -1
    end

    $happiness[[local_people[0], local_people[-1]]] = value
end

part1()
part2()