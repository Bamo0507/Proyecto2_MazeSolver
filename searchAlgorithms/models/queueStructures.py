class LIFO:
    def __init__(self):
        self.queue = []

    def empty(self):
        return len(self.queue) == 0

    def top(self):
        return self.queue[0]

    def pop(self):
        return self.queue.pop(0)

    def add(self, element):
        self.queue.insert(0, element)
        return self.queue


class FIFO:
    def __init__(self):
        self.queue = []

    def empty(self):
        return len(self.queue) == 0

    def top(self):
        return self.queue[0]

    def pop(self):
        return self.queue.pop(0)

    def add(self, element):
        self.queue.append(element)
        return self.queue


class Priority:
    def __init__(self):
        self.queue = []  # lista de tuplas (element, priority)

    def empty(self):
        return len(self.queue) == 0

    def top(self):
        return self.queue[0]

    def pop(self):
        return self.queue.pop(0)

    def add(self, element, priority):
        position = len(self.queue)  # por defecto va al final
        for i in range(len(self.queue)):
            if priority < self.queue[i][1]:  # menor valor es mejor porque queremos un camino corto
                position = i
                break
        self.queue.insert(position, (element, priority))
        return self.queue
