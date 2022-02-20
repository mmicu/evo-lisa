package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	fmt.Println("evo_lisa")

	// Color
	c := RandomColor()
	fmt.Println(c)
	c.Mutate()

	// Point
	p := RandomPoint(10, 10)
	fmt.Println(p)
	p.Mutate(10, 10)
}
