from __future__ import annotations

import itertools
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Iterable

from typing import ParamSpec

P = ParamSpec("P")
T = TypeVar("T")
U = TypeVar("U")


def batch(it: Iterable[T], by: int) -> Iterable[tuple[T, ...]]:
    """
    Chunk an iterable into tuples of a given size.

    >>> list(batch(range(11), 2))
    [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10,)]

    >>> list(batch([], 2))
    []
    """
    iterator = iter(it)
    while True:
        chunk = tuple(itertools.islice(iterator, by))
        if not chunk:
            break
        yield chunk
