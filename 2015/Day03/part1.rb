#!/usr/bin/env ruby
require 'set'

f = File.open("input.txt")
line = f.read()

coords = [0,0]
visited = Set[coords]
line.each_char do |c|
    case c
    when '<'
        coords = [coords[0]-1, coords[1]]
    when '>'
        coords = [coords[0]+1, coords[1]]
    when '^'
        coords = [coords[0], coords[1]+1]
    when 'v'
        coords = [coords[0], coords[1]-1]
    end

    visited << coords
end

puts visited.length