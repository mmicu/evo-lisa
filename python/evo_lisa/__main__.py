#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser, ArgumentTypeError
from copy import deepcopy
from datetime import timedelta
from math import inf
from os import listdir, path
from time import time as current_time

from evo_lisa.constants import (
    DEFAULT_LOG_LEVEL,
    DEFAULT_NUM_GENERATIONS,
    LOG_LEVELS,
)
from evo_lisa.population import Population
from evo_lisa.utils import (
    init_logger,
    g_logger,
)


def _existing_file(file_path: str) -> str:
    if path.isfile(file_path):
        return file_path

    raise ArgumentTypeError(f'file "{file_path}" does not exist')


def _writable_file(file_path: str) -> str:
    try:
        fd = open(file_path, 'w')
        fd.close()

        return file_path
    except BaseException:
        raise ArgumentTypeError(f'"{file_path}" is not a valid output location')


def _empty_directory(dir_path: str) -> str:
    if path.isdir(dir_path) and len(listdir(dir_path)):
        raise ArgumentTypeError(f'directory "{dir_path}" is not empty')

    return dir_path


def _get_arguments_parser() -> ArgumentParser:
    parser = ArgumentParser()

    # Target image
    parser.add_argument('image_path', type=_existing_file)

    # Output image
    parser.add_argument('output_image_path', type=_writable_file)

    # Log level
    parser.add_argument('-l', '--log_level', type=str, choices=LOG_LEVELS, default=DEFAULT_LOG_LEVEL, help='log level.')

    # Number of generations
    parser.add_argument('-n', '--generations', type=int, default=DEFAULT_NUM_GENERATIONS, help='number of generations.')

    return parser


def main() -> int:
    # Parse command line arguments
    args = _get_arguments_parser().parse_args()

    # Init logger
    init_logger(args.log_level)

    # Init population
    population = None
    try:
        population = Population(image_path=args.image_path, size=0)
    except BaseException as be:
        g_logger.error(f'Cannot initialize population. Reason: {str(be)}')
        return 1

    start = current_time()
    error = inf
    generation = selected = 0
    while generation < args.generations:
        # Try to apply mutations
        new_population = deepcopy(population)
        mut_occurs = new_population.mutate()
        if not mut_occurs:
            continue

        # Calculate error
        generation += 1
        new_error = new_population.calculate_error()
        if new_error < error:
            error = new_error
            population = new_population
            selected += 1

            g_logger.debug(f'New error: {new_error} ({generation + 1}/{args.generations}) - selected: {selected} - polygons: {len(population._polygons)}')

    elapsed = str(timedelta(seconds=current_time() - start))
    g_logger.debug(f'Elapsed: {elapsed}')

    # Draw result
    ok, err = population.draw(args.output_image_path)
    if err:
        g_logger.error(f'Cannot draw population. Reason: {err}')
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
