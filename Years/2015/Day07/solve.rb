def find_value(value)
    # base cases
    if value.to_s.match((/^\d+$/))
        return value.to_i
    end

    if $data[value].length == 1 && $data[value][0].match((/^\d+$/))
        return $data[value][0].to_i
    end

    # recursive calls
    if $data[value].include? "NOT"
        output = ~find_value($data[value][1]) & 65535

    elsif $data[value].include? "AND"
        output = find_value($data[value][0]) & find_value($data[value][2])

    elsif $data[value].include? "OR"
        output = find_value($data[value][0]) | find_value($data[value][2])

    elsif $data[value].include? "RSHIFT"
        output = find_value($data[value][0]) >> find_value($data[value][2])

    elsif $data[value].include? "LSHIFT"
        output = find_value($data[value][0]) << find_value($data[value][2])

    else
        output = find_value($data[value][0])
    end

    # momoize previously found values
    $data[value] = [output.to_s]
    return output
end

def part1(local_data)
    $data = local_data
    return find_value("a")
end

def part2(local_data, p1_answer)
    local_data["b"] = [p1_answer.to_s]
    $data = local_data
    
    return find_value("a")
end

lines = File.readlines('input.txt')

data1 = Hash.new
data2 = Hash.new
for line in lines do
    line = line.split(" ")
    data1[line.last] = line[0..-3]
    data2[line.last] = line[0..-3]
end

p1_answer = part1(data1)
p2_answer = part2(data2, p1_answer)

p p1_answer
p p2_answer