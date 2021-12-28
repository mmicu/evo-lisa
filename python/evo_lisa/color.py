#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from typing import Dict

from evo_lisa.constants import (
    PROBABILITY_UPDATE_BLUE_COLOR,
    PROBABILITY_UPDATE_GREEN_COLOR,
    PROBABILITY_UPDATE_RED_COLOR,
)
from evo_lisa.utils import (
    Mutation,
    apply_mutations,
)


class RGB:
    def __init__(self, r: int, g: int, b: int) -> None:
        self._r = r
        self._g = g
        self._b = b

    def _mutate_red(self) -> None:
        self._r = RGB.random_color()

    def _mutate_green(self) -> None:
        self._g = RGB.random_color()

    def _mutate_blue(self) -> None:
        self._b = RGB.random_color()

    def mutate(self) -> bool:
        args: Dict[object, object] = dict()

        return apply_mutations(mutations=[
            Mutation(function=self._mutate_red,   args=args, probability=PROBABILITY_UPDATE_RED_COLOR),
            Mutation(function=self._mutate_green, args=args, probability=PROBABILITY_UPDATE_GREEN_COLOR),
            Mutation(function=self._mutate_blue,  args=args, probability=PROBABILITY_UPDATE_BLUE_COLOR),
        ])

    @property
    def r(self) -> int:
        return self._r

    @property
    def g(self) -> int:
        return self._g

    @property
    def b(self) -> int:
        return self._b

    @staticmethod
    def random_color() -> int:
        return randint(0, 255)

    @staticmethod
    def random() -> 'RGB':
        return RGB(
            r=RGB.random_color(),
            g=RGB.random_color(),
            b=RGB.random_color(),
        )
