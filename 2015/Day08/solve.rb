def part1(lines)
    p lines.map { |line| line.length - eval(line).length }.sum
end

def part2(lines)
    p lines.map { |line| line.count('\\') + line.count('"') + 2}.sum
end


lines = File.readlines('input.txt').map { |line| line.chomp}

part1(lines)
part2(lines)