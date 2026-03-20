import time
from loadMaze.maze import Maze
from searchAlgorithms.models.node import Node
from searchAlgorithms.models.queueStructures import FIFO
from searchAlgorithms.models.searchResult import SearchResult
from searchAlgorithms.utils import reconstruct_path, ACTIONS


def bfs(maze: Maze, start: tuple[int, int], goal: tuple[int, int]) -> SearchResult:
    exploredPending = FIFO()
    explored = set()

    start_node = Node(state=start)
    exploredPending.add(start_node)

    nodes_explored = 0
    total_neighbors = 0

    start_time = time.time()

    while not exploredPending.empty():
        current_node = exploredPending.pop()

        if current_node.state == goal:
            # encontramos la meta, calculamos branching factor y retornamos
            end_time = time.time()
            branching_factor = total_neighbors / nodes_explored if nodes_explored > 0 else 0
            return SearchResult(
                path=reconstruct_path(current_node),
                nodes_explored=nodes_explored,
                execution_time=end_time - start_time,
                branching_factor=branching_factor
            )

        if current_node.state in explored:
            # no repetimos nodos ya explorados
            continue

        explored.add(current_node.state)
        nodes_explored += 1

        for action in ACTIONS:
            new_row = current_node.state[0] + action[0]
            new_col = current_node.state[1] + action[1]

            if maze.is_walkable(new_row, new_col) and (new_row, new_col) not in explored:
                neighbor_node = Node(
                    state=(new_row, new_col),
                    parent=current_node,
                    action=action,
                    path_cost=current_node.path_cost + 1
                )
                exploredPending.add(neighbor_node)
                total_neighbors += 1
