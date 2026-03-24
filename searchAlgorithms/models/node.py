from dataclasses import dataclass, field
from typing import Any

@dataclass
class Node:
    state: Any
    parent: "Node | None" = field(default=None)  # si es raiz, no hay padre
    action: Any = field(default=None) # la accion que se tomo para llegar a este estado
    path_cost: float = field(default=0.0) # el costo acumulado desde la raiz hasta este nodo
