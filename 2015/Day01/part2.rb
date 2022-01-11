#!/usr/bin/env ruby

if __FILE__ == $0
  file = File.open("./input.txt")
  file_data = file.read

  chars = file_data.split('')

  floor = 0
  idx = 0
  done = false
  chars.each { |c|
    idx += 1
    if c == "("
      floor += 1
    else
      floor -= 1
    end
    if floor < 0 and done == false
      puts idx
      done = true
    end
  }
end