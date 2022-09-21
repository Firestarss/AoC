package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"strconv"
)

func match_hash(key, match string) {
	counter := 0
	for {
		test := key + strconv.Itoa(counter)

		h := md5.New()
		io.WriteString(h, test)

		hash := hex.EncodeToString(h.Sum(nil))

		if hash[0:len(match)] == match {
			fmt.Println(counter)
			break
		}
		counter++
	}
}

func main() {
	key := "yzbqklnj"
	match_hash(key, "00000")
	match_hash(key, "000000")
}
