package main

import (
	"fmt"
	"io/ioutil"
)

const file = "input"

//const file = "test_input"

type coord struct {
	posX int
	posY int
}

func main() {
	part1()
}

func part1() {
	var (
		grid    coord
		houses  int
		visited []coord
	)

	fbyte, _ := ioutil.ReadFile(file)
	fcontents := string(fbyte)

	for _, e := range fcontents {
		switch e {
		case '^':
			grid.posY++
		case 'v':
			grid.posY--
		case '>':
			grid.posX++
		case '<':
			grid.posX--
		}
		visited = append(visited, grid)
	}
	for i := 0; i < len(visited); i++ {
		houses++
	}
	fmt.Println(visited)
	fmt.Println("final position: ", grid)
	fmt.Println("houses: ", houses)
}
