import math
from searchAlgorithms.models.node import Node

# jerarquia de movimientos: arriba, derecha, abajo, izquierda
ACTIONS = [
    (-1, 0),  # arriba
    (0, 1),   # derecha
    (1, 0),   # abajo
    (0, -1),  # izquierda
]


def manhattan(current: tuple[int, int], goal: tuple[int, int]) -> float:
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def euclidean(current: tuple[int, int], goal: tuple[int, int]) -> float:
    return math.sqrt((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2)


def reconstruct_path(node: Node) -> list[tuple[int, int]]:
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path
