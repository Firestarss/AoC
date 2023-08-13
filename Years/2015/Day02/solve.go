package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func part1(data []string) {
	total := 0

	for i := 0; i < len(data); i++ {
		lengths := strings.Split(data[i], "x")
		l, _ := strconv.Atoi(lengths[0])
		w, _ := strconv.Atoi(lengths[1])
		h, _ := strconv.Atoi(lengths[2])

		sides := [3]int{l * w, w * h, h * l}
		min := sides[0]

		for j := 0; j < len(sides); j++ {
			if sides[j] < min {
				min = sides[j]
			}
		}
		total += (sides[0]+sides[1]+sides[2])*2 + min
	}
	fmt.Println(total)
}

func part2(data []string) {
	total := 0

	for i := 0; i < len(data); i++ {
		lengths := strings.Split(data[i], "x")
		l, _ := strconv.Atoi(lengths[0])
		w, _ := strconv.Atoi(lengths[1])
		h, _ := strconv.Atoi(lengths[2])

		sides := [3]int{l + w, w + h, h + l}
		vol := l * w * h
		min := sides[0]

		for j := 0; j < len(sides); j++ {
			if sides[j] < min {
				min = sides[j]
			}
		}
		total += min*2 + vol
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
