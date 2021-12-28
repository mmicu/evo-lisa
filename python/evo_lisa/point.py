#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

from evo_lisa.constants import (
    PROBABILITY_MOVE_MAX_POINT,
    PROBABILITY_MOVE_MID_POINT,
    PROBABILITY_MOVE_MIN_POINT,
)
from evo_lisa.utils import (
    Mutation,
    apply_mutations,
)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def _mutate_move_0(self, max_width: int, max_height: int) -> None:
        self._x = randint(0, max_width)
        self._y = randint(0, max_height)

    def _mutate_move_1(self, max_width: int, max_height: int) -> None:
        kx = (max_width * 10) // 100
        ky = (max_height * 10) // 100
        self._x = min(max(0, self._x + randint(-kx, kx)), max_width)
        self._y = min(max(0, self._y + randint(-ky, ky)), max_height)

    def _mutate_move_2(self, max_width: int, max_height: int) -> None:
        kx = (max_width * 2) // 100
        ky = (max_height * 2) // 100
        self._x = min(max(0, self._x + randint(-kx, kx)), max_width)
        self._y = min(max(0, self._y + randint(-ky, ky)), max_height)

    def mutate(self, max_width: int, max_height: int) -> bool:
        args = dict(max_width=max_width, max_height=max_height)

        return apply_mutations(mutations=[
            Mutation(function=self._mutate_move_0, args=args, probability=PROBABILITY_MOVE_MAX_POINT),
            Mutation(function=self._mutate_move_1, args=args, probability=PROBABILITY_MOVE_MID_POINT),
            Mutation(function=self._mutate_move_2, args=args, probability=PROBABILITY_MOVE_MIN_POINT),
        ])

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @staticmethod
    def random(max_width: int, max_height: int) -> 'Point':
        return Point(x=randint(0, max_width), y=randint(0, max_height))
