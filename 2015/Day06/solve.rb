def part1(data)
    lights = Array.new(1000) {Array.new(1000) {0}}

    for line in data do
        coords = line.scan(/\d+/)

        if line.include? "on"
            instruction = "on"
        elsif line.include? "off"
            instruction = "off"
        elsif line.include? "toggle"
            instruction = "toggle"
        end

        for i in (coords[0].to_i..coords[2].to_i)
            for j in (coords[1].to_i..coords[3].to_i)
                if instruction == "on"
                    lights[i][j] = 1
                elsif instruction == "off"
                    lights[i][j] = 0
                elsif instruction == "toggle"
                    lights[i][j] = (lights[i][j] + 1) % 2
                end
            end
        end

    end
    total = 0
    for row in lights
        for col in row
            total = total + col
        end
    end
    puts total
end

def part2(data)
    lights = Array.new(1000) {Array.new(1000) {0}}

    for line in data do
        coords = line.scan(/\d+/)

        if line.include? "on"
            instruction = "on"
        elsif line.include? "off"
            instruction = "off"
        elsif line.include? "toggle"
            instruction = "toggle"
        end

        for i in (coords[0].to_i..coords[2].to_i)
            for j in (coords[1].to_i..coords[3].to_i)
                if instruction == "on"
                    lights[i][j] = lights[i][j] + 1
                elsif instruction == "off"
                    lights[i][j] = lights[i][j] - 1
                    if lights[i][j] < 0
                        lights[i][j] = 0
                    end
                elsif instruction == "toggle"
                    lights[i][j] = lights[i][j] + 2
                end
            end
        end

    end
    total = 0
    for row in lights
        for col in row
            total = total + col
        end
    end
    puts total
end

data = File.readlines('input.txt')

part1(data)
part2(data)