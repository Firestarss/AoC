package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

func part1(data []string) {
	var lights [1000][1000]int
	coords_r := regexp.MustCompile("[0-9]+")
	inst_r := regexp.MustCompile("on|off|toggle")

	for i := 0; i < len(data); i++ {
		coords := coords_r.FindAllString(data[i], -1)
		inst := inst_r.FindAllString(data[i], 1)
		x1, _ := strconv.Atoi(coords[0])
		y1, _ := strconv.Atoi(coords[1])
		x2, _ := strconv.Atoi(coords[2])
		y2, _ := strconv.Atoi(coords[3])

		for x := x1; x <= x2; x++ {
			for y := y1; y <= y2; y++ {
				if inst[0] == "on" {
					lights[x][y] = 1
				}
				if inst[0] == "off" {
					lights[x][y] = 0
				}
				if inst[0] == "toggle" {
					lights[x][y] = (lights[x][y] + 1) % 2
				}
			}
		}
	}

	total := 0
	for i := 0; i < 1000; i++ {
		for j := 0; j < 1000; j++ {
			total += lights[i][j]
		}
	}
	fmt.Println(total)
}

func part2(data []string) {
	var lights [1000][1000]int
	coords_r := regexp.MustCompile("[0-9]+")
	inst_r := regexp.MustCompile("on|off|toggle")

	for i := 0; i < len(data); i++ {
		coords := coords_r.FindAllString(data[i], -1)
		inst := inst_r.FindAllString(data[i], 1)
		x1, _ := strconv.Atoi(coords[0])
		y1, _ := strconv.Atoi(coords[1])
		x2, _ := strconv.Atoi(coords[2])
		y2, _ := strconv.Atoi(coords[3])

		for x := x1; x <= x2; x++ {
			for y := y1; y <= y2; y++ {
				if inst[0] == "on" {
					lights[x][y] += 1
				}
				if inst[0] == "off" {
					lights[x][y] -= 1
					if lights[x][y] < 0 {
						lights[x][y] = 0
					}
				}
				if inst[0] == "toggle" {
					lights[x][y] += 2
				}
			}
		}
	}

	total := 0
	for i := 0; i < 1000; i++ {
		for j := 0; j < 1000; j++ {
			total += lights[i][j]
		}
	}
	fmt.Println(total)
}

func main() {

	input, err := ioutil.ReadFile("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	data := strings.Split(string(input), "\n")

	part1(data)
	part2(data)
}
