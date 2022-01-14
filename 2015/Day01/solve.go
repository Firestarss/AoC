package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func part1(data string) {
	total := 0

	for i := 0; i < len(data); i++ {
		if data[i] == '(' {
			total += 1
		}
		if data[i] == ')' {
			total -= 1
		}
	}
	fmt.Println(total)
}

func part2(data string) {
	total := 0

	for i := 0; i < len(data); i++ {
		if data[i] == '(' {
			total += 1
		}
		if data[i] == ')' {
			total -= 1
		}

		if total < 0 {
			fmt.Println(i + 1)
			break
		}
	}
}

func main() {

	data, err := ioutil.ReadFile("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	part1(string(data)) // 232
	part2(string(data)) // 1783
}
