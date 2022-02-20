package main

import (
	"math/rand"
)

func WillMutate(rate int) bool {
	return rand.Intn(rate+1) == rate
}
