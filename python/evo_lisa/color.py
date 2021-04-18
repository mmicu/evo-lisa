#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from typing import Dict

from evo_lisa.settings import PROBABILITY_UPDATE_RED_COLOR, PROBABILITY_UPDATE_GREEN_COLOR, \
    PROBABILITY_UPDATE_BLUE_COLOR, PROBABILITY_UPDATE_ALPHA_LEVEL
from evo_lisa.utils import apply_mutations, Mutation


class RGBA:
    def __init__(self, r: int, g: int, b: int, a: int) -> None:
        self._r = r
        self._g = g
        self._b = b
        self._a = a

    def _mutate_red(self) -> None:
        self._r = RGBA.random_color()

    def _mutate_green(self) -> None:
        self._g = RGBA.random_color()

    def _mutate_blue(self) -> None:
        self._b = RGBA.random_color()

    def _mutate_alpha(self) -> None:
        self._a = RGBA.random_alpha()

    def mutate(self) -> bool:
        args: Dict[object, object] = dict()

        return apply_mutations(mutations=[
            Mutation(function=self._mutate_red,   args=args, probability=PROBABILITY_UPDATE_RED_COLOR),
            Mutation(function=self._mutate_green, args=args, probability=PROBABILITY_UPDATE_GREEN_COLOR),
            Mutation(function=self._mutate_blue,  args=args, probability=PROBABILITY_UPDATE_BLUE_COLOR),
            Mutation(function=self._mutate_alpha, args=args, probability=PROBABILITY_UPDATE_ALPHA_LEVEL),
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

    @property
    def a(self) -> int:
        return self._a

    @staticmethod
    def random_color() -> int:
        return randint(0, 255)

    @staticmethod
    def random_alpha() -> int:
        return randint(30, 60)

    @staticmethod
    def random() -> 'RGBA':
        return RGBA(r=RGBA.random_color(), g=RGBA.random_color(), b=RGBA.random_color(), a=RGBA.random_alpha())
