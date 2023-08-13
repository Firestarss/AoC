require 'set'

def eval_dist(stops)
    total = 0
    for i in (0..stops.length-2)
        total += $distances[[stops[i], stops[i+1]]]
    end
    return total
end

def part1()
    p Array(Array($places).permutation($places.length)).map { |stops| eval_dist(stops)}.min
end

def part2()
    p Array(Array($places).permutation($places.length)).map { |stops| eval_dist(stops)}.max
end
    
lines = File.readlines('input.txt')

$places = Set.new
$distances = Hash.new

for line in lines
    local_places = line.scan(/[a-zA-Z]+/)
    $places = $places | [local_places[0], local_places[2]]

    $distances[[local_places[0], local_places[2]]] = line.match(/\d+/)[0].to_i
    $distances[[local_places[2], local_places[0]]] = line.match(/\d+/)[0].to_i
end

part1()
part2()