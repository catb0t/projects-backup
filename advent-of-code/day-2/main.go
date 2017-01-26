package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

//const inputFile = "test_input"

const inputFile = "input"

func main() {
	Part1()
	Part2()
}

//Min finds the minimum of a list of numbers
func Min(v1 int, vn ...int) (m int) {
	m = v1
	for i := 0; i < len(vn); i++ {
		if vn[i] < m {
			m = vn[i]
		}
	}
	return
}

//Total sums a list of numbers
func Total(list []int) (sum int) {
	for _, e := range list {
		sum += e
	}
	return
}

//Part1 of challenge
func Part1() {
	var (
		final             []int
		a, b, c, smallest int
	)
	file, _ := ioutil.ReadFile(inputFile)
	input := strings.Split(string(file), "\n")
	input = input[:len(input)-1]
	for _, e := range input {
		dims := strings.Split(e, "x")
		var vals []int
		for _, e := range dims {
			asInt, _ := strconv.Atoi(e)
			vals = append(vals, asInt)
		}
		for i := 0; i < len(vals); i++ {
			a = (vals[0] * vals[1]) * 2
			b = (vals[1] * vals[2]) * 2
			c = (vals[2] * vals[0]) * 2
			smallest = Min(a, b, c) / 2
		}
		final = append(final, (a + b + c + smallest))
	}
	//fmt.Println(final)
	fmt.Println("part1")
	fmt.Println("last smallest:", smallest)
	check := len(final) == len(input)
	fmt.Println(check)
	fmt.Println(Total(final))
}

//Part2 of challenge
func Part2() {
	var (
		final                     []int
		a, b, c, volume, smallest int
	)
	file, _ := ioutil.ReadFile(inputFile)
	input := strings.Split(string(file), "\n")
	input = input[:len(input)-1]
	for _, e := range input {
		dims := strings.Split(e, "x")
		var vals []int
		for _, e := range dims {
			asInt, _ := strconv.Atoi(e)
			vals = append(vals, asInt)
		}
		for i := 0; i < len(vals); i++ {
			a = (vals[0]*2 + vals[1]*2)
			b = (vals[1]*2 + vals[2]*2)
			c = (vals[2]*2 + vals[0]*2)
			volume = vals[0] * vals[1] * vals[2]
			smallest = Min(a, b, c) // / 2
		}
		final = append(final, (smallest + volume))
	}
	//fmt.Println(final)
	fmt.Println("\npart2")
	fmt.Println("last smallest:", smallest)
	fmt.Println("last volume:", volume)
	check := len(final) == len(input)
	fmt.Println(check)
	fmt.Println(Total(final))
}
