def part1(data)
  puts data.count('(') - data.count(')')
end

def part2(data)
  floor = 0
  data.each_char.with_index do |char, i|
    floor = char == '(' ? floor + 1 : floor - 1
    if floor < 0
      puts i + 1
      break
    end
  end
end

data = File.read("../input.txt")
part1(data)
part2(data)
