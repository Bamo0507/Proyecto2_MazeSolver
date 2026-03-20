from dataclasses import dataclass


@dataclass
class SearchResult:
    path: list[tuple[int, int]]
    nodes_explored: int
    execution_time: float
    branching_factor: float
    explored_order: list[tuple[int, int]]
