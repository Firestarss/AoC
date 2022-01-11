#!/usr/bin/env ruby

if __FILE__ == $0
  file = File.open("./input.txt")
  file_data = file.read

  puts file_data.count("(") - file_data.count(")")
end