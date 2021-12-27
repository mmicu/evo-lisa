#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from collections import namedtuple
from random import choices
from typing import List

from evo_lisa.constants import LOG_LEVELS

Mutation = namedtuple('Mutation', ['function', 'args', 'probability'])
g_logger = logging.getLogger('evo_lisa')


def init_logger(level: str) -> None:
    assert level in LOG_LEVELS, f'unknown level "{level}"'

    global g_logger

    if not g_logger:
        g_logger = logging.getLogger(__name__)

    g_logger.setLevel(level)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_format)

    g_logger.addHandler(stream_handler)


def will_mutate(probability: float) -> bool:
    assert 0 <= probability <= 1, f'{probability} not in [0, 1]'

    return choices(population=[True, False], weights=[probability, 1 - probability])[0]


def apply_mutations(mutations: List[Mutation]) -> bool:
    mut_occurs = False

    for mutation in mutations:
        if will_mutate(mutation.probability):
            if not mut_occurs:
                mut_occurs = True

            mutation.function(**mutation.args)

    return mut_occurs
