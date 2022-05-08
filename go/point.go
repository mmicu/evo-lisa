package main

import (
	"math/rand"
)

type Point struct {
	x, y int
}

func (p *Point) Mutate(max_width, max_height int) bool {
	has_mutated := false

	// First mutation
	if WillMutate(MutationRateMaxMovePoint) {
		p.x = rand.Intn(max_width + 1)
		p.y = rand.Intn(max_height + 1)

		has_mutated = true
	}

	// Second mutation
	if WillMutate(MutationRateMidMovePoint) {
		var kx int = 20
		var ky int = 20
		p.x = min(max(0, p.x+randInt(-kx, +kx+1)), max_width)
		p.y = min(max(0, p.y+randInt(-ky, +ky+1)), max_height)

		has_mutated = true
	}

	// Third mutation
	if WillMutate(MutationRateMinMovePoint) {
		var kx int = 3
		var ky int = 3
		p.x = min(max(0, p.x+randInt(-kx, +kx+1)), max_width)
		p.y = min(max(0, p.y+randInt(-ky, +ky+1)), max_height)

		has_mutated = true
	}

	return has_mutated
}

func RandomPoint(max_width, max_height int) *Point {
	return &Point{
		x: rand.Intn(max_width + 1),
		y: rand.Intn(max_height + 1),
	}
}

func randInt(min, max int) int {
	return min + rand.Intn(max-min)
}

func min(x, y int) int {
	if x < y {
		return x
	}

	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}

	return y
}
