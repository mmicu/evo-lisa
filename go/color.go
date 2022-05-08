package main

import (
	"math/rand"
)

type Color struct {
	r uint8
	g uint8
	b uint8
}

func (c *Color) Mutate() bool {
	has_mutated := false

	// r
	if WillMutate(MutationRateUpdateRedColor) {
		c.r = randomColorValue()
		has_mutated = true
	}

	// g
	if WillMutate(MutationRateUpdateGreenColor) {
		c.g = randomColorValue()
		has_mutated = true
	}

	// b
	if WillMutate(MutationRateUpdateBlueColor) {
		c.b = randomColorValue()
		has_mutated = true
	}

	return has_mutated
}

func RandomColor() *Color {
	return &Color{
		r: randomColorValue(),
		g: randomColorValue(),
		b: randomColorValue(),
	}
}

func randomColorValue() uint8 {
	return uint8(rand.Intn(256))
}
