package main

import (
	"fmt"
	"regexp"
)

func increment_pass(password string) (output string) {
	output = password[:len(password)-1]
	last_char := string(int(password[len(password)-1]) + 1)

	if last_char == "{" {
		last_char = "a"
		output = increment_pass(output)
	}
	output += last_char
	return
}

func is_valid(password string) (output bool) {
	has_straight := false
	has_illegals, _ := regexp.MatchString("i|o|l", password)
	doubles := 0

	for i := 0; i < len(password)-2; i++ {
		if password[i] == password[i+1]-1 && password[i] == password[i+2]-2 {
			has_straight = true
		}
	}

	for i := 0; i < len(password)-1; i++ {
		if password[i] == password[i+1] {
			i++
			doubles++
		}
	}
	output = has_straight && !has_illegals && doubles >= 2
	return
}

func next_password(password string) string {
	for {
		password = increment_pass(password)
		if is_valid((password)) {
			fmt.Println(password)
			break
		}
	}
	return password
}

func main() {
	p1_ans := next_password("vzbxkghb")
	next_password(p1_ans)
}
