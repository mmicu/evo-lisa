package main

const (
	DEFAULT_ITERATIONS = 100_000

	MutationRateUpdateRedColor   = 1500
	MutationRateUpdateGreenColor = 1500
	MutationRateUpdateBlueColor  = 1500

	MutationRateMaxMovePoint = 1500
	MutationRateMidMovePoint = 1500
	MutationRateMinMovePoint = 1500

	PROBABILITY_ADD_POLYGON    = float32(1) / float32(700)
	PROBABILITY_REMOVE_POLYGON = float32(1) / float32(1_500)
	PROBABILITY_MOVE_POLYGON   = float32(1) / float32(700)

	PROBABILITY_MOVE_MIN_POINT = float32(1) / float32(1_500)
	PROBABILITY_MOVE_MID_POINT = float32(1) / float32(1_500)
	PROBABILITY_MOVE_MAX_POINT = float32(1) / float32(1_500)

	PROBABILITY_ADD_POINT    = float32(1) / float32(1_500)
	PROBABILITY_REMOVE_POINT = float32(1) / float32(1_500)

	MIN_POINTS_PER_POLYGON = 3
	MAX_POINTS_PER_POLYGON = 10

	MIN_ACTIVE_POINTS = 0
	MAX_ACTIVE_POINTS = 1_500

	MIN_POLYGONS = 0
	MAX_POLYGONS = 255
)
