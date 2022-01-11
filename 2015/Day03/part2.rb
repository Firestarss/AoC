#!/usr/bin/env ruby
require 'set'

f = File.open("input.txt")
line = f.read()

santa_coords = [0,0]
robo_coords = [0,0]
agent = [santa_coords, robo_coords]
visited = Set[santa_coords]

counter = 0
line.each_char do |c|
    idx = counter % 2
    case c
    when '<'
        agent[idx] = [agent[idx][0]-1, agent[idx][1]]
    when '>'
        agent[idx] = [agent[idx][0]+1, agent[idx][1]]
    when '^'
        agent[idx] = [agent[idx][0], agent[idx][1]+1]
    when 'v'
        agent[idx] = [agent[idx][0], agent[idx][1]-1]
    end

    counter = counter + 1
    visited << agent[idx]
end

puts visited.length