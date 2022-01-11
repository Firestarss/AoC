#!/usr/bin/env ruby

if __FILE__ == $0
    total = 0
    File.readlines('input.txt').each do |line|
      line = line.split("x")

      for i in 0..line.length() do
        line[i] = line[i].to_i
      end
      
      sides = [line[0] + line[1], line[1] + line[2], line[2] + line[0]]
      vol = line[0] * line[1] * line[2]

      local_total = sides.min * 2 + vol

      total += local_total
    end

    puts total
  end