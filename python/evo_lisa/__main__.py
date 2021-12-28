#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import (
    ArgumentParser,
    ArgumentTypeError,
)
from copy import deepcopy
from datetime import timedelta
from math import inf
from os import listdir, path
from time import time as current_time

from evo_lisa.constants import (
    DEFAULT_ITERATIONS,
    DEFAULT_LOG_LEVEL,
    LOG_LEVELS,
)
from evo_lisa.population import (
    Population,
)
from evo_lisa.utils import (
    g_logger,
    init_logger,
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

    # Number of iterations
    parser.add_argument('-n', '--iterations', type=int, default=DEFAULT_ITERATIONS, help='number of iterations.')

    return parser


def _main() -> int:
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
    gen = selected_gen = 0
    for iteration in range(1, args.iterations + 1):
        # Try to apply mutations
        new_population = deepcopy(population)
        mut_occurs = new_population.mutate()
        if not mut_occurs:
            continue

        gen += 1

        # Calculate error
        new_error = new_population.calculate_error()
        if new_error < error:
            error = new_error
            population = new_population
            selected_gen += 1

            g_logger.debug(f'New error: {new_error} - iteration: {iteration}/{args.iterations} - mutated generations: {gen} - selected: {selected_gen} - polygons: {len(population._polygons)}')

    elapsed = str(timedelta(seconds=current_time() - start))
    g_logger.debug(f'Elapsed: {elapsed}')

    # Draw result
    _, err = population.draw(args.output_image_path)
    if err:
        g_logger.error(f'Cannot draw population. Reason: {err}')
        return 1

    return 0


if __name__ == '__main__':
    exit(_main())
