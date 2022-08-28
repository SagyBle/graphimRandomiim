from component import Component


class Vertice:
    def __init__(self, key: int, data):
        self.key = key
        self.data = data
        self.neighbors = []
        self.component = Component({self})

    def get_key(self):
        return self.key

    # Add neighbor to vertice neighbors set, if neighbor isn't exist there already.
    def add_neighbour(self, neighbor):
        if isinstance(neighbor, Vertice):
            self.neighbors.append(neighbor) if neighbor not in self.neighbors else self.neighbors
            neighbor.neighbors.append(self) if self not in neighbor.neighbors else neighbor.neighbors
        else:
            raise Exception("Vertice neighbour should be a Vertice instance only.")

    def print_neighbours(self):
        if len(self.neighbors) == 0:
            print("{}")
        else:
            output = "{"
            for v in self.neighbors:
                output = output + str(v.key) + ', '
            print(output[:-2] + '}')
