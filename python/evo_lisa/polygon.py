#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from typing import List

from evo_lisa.color import RGB
from evo_lisa.point import Point
from evo_lisa.constants import (
    MIN_POINTS_PER_POLYGON,
    PROBABILITY_REMOVE_POINT,
    PROBABILITY_ADD_POINT,
    MAX_POINTS_PER_POLYGON,
    MIN_ACTIVE_POINTS,
    MAX_ACTIVE_POINTS,
)
from evo_lisa.utils import (
    apply_mutations,
    Mutation,
)


class Polygon:
    def __init__(self, origin: Point, points: List[Point], color: RGB) -> None:
        self._origin = origin
        self._points = points
        self._color = color

    def _add_mutate(self, population_points: int) -> None:
        if len(self._points) > 1 and len(self._points) < MAX_POINTS_PER_POLYGON and population_points < MAX_ACTIVE_POINTS:
            index = randint(1, len(self._points) - 1)

            prev = self._points[index - 1]
            next = self._points[index]

            point = Point(x=(prev.x + next.x) // 2, y=(prev.y + next.y) // 2)
            self._points.insert(index, point)

    def _remove_mutate(self, population_points: int) -> None:
        if len(self._points) > MIN_POINTS_PER_POLYGON and population_points > MIN_ACTIVE_POINTS:
            index = randint(0, len(self._points) - 1)
            del self._points[index]

    def mutate(self, max_width: int, max_height: int, population_points: int) -> bool:
        # Apply main mutation
        mut_occurs = apply_mutations(mutations=[
            Mutation(function=self._add_mutate,    args=dict(population_points=population_points), probability=PROBABILITY_ADD_POINT),
            Mutation(function=self._remove_mutate, args=dict(population_points=population_points), probability=PROBABILITY_REMOVE_POINT),
        ])

        # Apply color mutation
        color_mut_occurs = self._color.mutate()

        # Apply mutation for each point
        points_mutation_occurs = False
        for point in self._points:
            if point.mutate(max_width, max_height):
                points_mutation_occurs = True

        return mut_occurs or color_mut_occurs or points_mutation_occurs

    @property
    def origin(self) -> Point:
        return self._origin

    @property
    def points(self) -> List[Point]:
        return self._points

    @property
    def color(self) -> RGB:
        return self._color

    @staticmethod
    def random(max_width: int, max_height: int) -> 'Polygon':
        origin = Point.random(max_width=max_width, max_height=max_height)
        kx = (max_width * 2) // 100
        ky = (max_height * 2) // 100
        points = []
        for _ in range(MIN_POINTS_PER_POLYGON):
            x = min(max(0, origin.x + randint(-kx, +kx)), max_width)
            y = min(max(0, origin.y + randint(-ky, +ky)), max_height)

            points.append(Point(x=x, y=y))

        return Polygon(origin=origin, points=points, color=RGB.random())
