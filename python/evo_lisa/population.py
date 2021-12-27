#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from typing import List, Optional, Tuple

from PIL import (
    Image,
    ImageDraw,
)

from evo_lisa.polygon import Polygon
from evo_lisa.constants import (
    MAX_POLYGONS,
    PROBABILITY_ADD_POLYGON,
    PROBABILITY_REMOVE_POLYGON,
    PROBABILITY_MOVE_POLYGON,
)
from evo_lisa.utils import (
    apply_mutations,
    g_logger,
    Mutation,
)

g_image_cache: List[List[Tuple[float, float, float]]] = []


class Population:
    IMAGE_MODE = 'RGB'

    def __init__(self, image_path: str, size: int) -> None:
        self._image_path = image_path
        self._initial_size = size

        # Additional attributes
        self._image = None
        self._image_width = 0
        self._image_height = 0
        self._polygons: List[Polygon] = []

        # Load target image
        _, err = self._init()
        if err:
            raise BaseException(err)

    def _init(self) -> Tuple[bool, Optional[str]]:
        try:
            self._image = Image.open(self._image_path).convert(Population.IMAGE_MODE)
            self._image_width, self._image_height = self._image.size  # type: ignore
            self._polygons = [Polygon.random(self._image_width, self._image_height) for _ in range(self._initial_size)]
        except BaseException as be:
            return True, str(be)

        return True, None

    def _add_mutate(self) -> None:
        if len(self._polygons) < MAX_POLYGONS:
            new_polygon = Polygon.random(max_width=self._image_width, max_height=self._image_height)
            index = randint(0, len(self._polygons))

            self._polygons.insert(index, new_polygon)

    def _remove_mutate(self) -> None:
        if len(self._polygons):
            index = randint(0, len(self._polygons) - 1)
            del self._polygons[index]

    def _move_mutate(self) -> None:
        if len(self._polygons):
            index = randint(0, len(self._polygons) - 1)

            polygon = self._polygons[index]
            del self._polygons[index]

            index = randint(0, len(self._polygons))
            self._polygons.insert(index, polygon)

    def calculate_error(self) -> float:
        # Initialize image cache
        global g_image_cache
        if not g_image_cache:
            g_logger.debug('Loading input image cache')

            for i in range(self._image_width):
                col = []
                for j in range(self._image_height):
                    col.append(self._image.getpixel((i, j)))  # type: ignore

                g_image_cache.append(col)

        generated_image = self.generate_image()

        # Calculate error
        err = 0.0
        for i in range(self._image_width):
            for j in range(self._image_height):
                r0, g0, b0 = generated_image.getpixel((i, j))  # type: ignore
                r1, g1, b1 = g_image_cache[i][j]

                r = r0 - r1
                g = g0 - g1
                b = b0 - b1

                err += r * r + g * g + b * b

        return err

    def mutate(self) -> bool:
        # Apply main mutation
        mut_occurs = apply_mutations(mutations=[
            Mutation(function=self._add_mutate,    args=dict(), probability=PROBABILITY_ADD_POLYGON),
            Mutation(function=self._remove_mutate, args=dict(), probability=PROBABILITY_REMOVE_POLYGON),
            Mutation(function=self._move_mutate,   args=dict(), probability=PROBABILITY_MOVE_POLYGON),
        ])

        # Update counter of points in the entire population
        population_points = sum(len(polygon.points) for polygon in self._polygons)

        # Apply mutation to each polygon
        polygons_mut_occurs = False
        for polygon in self._polygons:
            has_mut = polygon.mutate(max_width=self._image_width, max_height=self._image_height, population_points=population_points)
            if has_mut and not polygons_mut_occurs:
                polygons_mut_occurs = True

        return mut_occurs or polygons_mut_occurs

    def generate_image(self) -> object:
        mode = Population.IMAGE_MODE
        image = Image.new(mode=mode, size=(self._image_width, self._image_height), color=(0, 0, 0))
        image_draw = ImageDraw.Draw(image, mode)

        for polygon in self._polygons:
            points = [(p.x, p.y) for p in polygon.points]
            image_draw.polygon(points, (polygon.color.r, polygon.color.g, polygon.color.b))

        return image

    def draw(self, path: str) -> Tuple[bool, Optional[str]]:
        image = self.generate_image()

        try:
            image.save(path, 'PNG')  # type: ignore
        except BaseException as be:
            return False, str(be)

        return True, None
