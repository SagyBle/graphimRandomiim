from component import Component


class Vertice:
    def __init__(self, key: int, data):
        self.key = key
        self.data = data
        self.neighbors = []
        self.component = Component({self})

    # def __eq__(self, other):
    #     return ((self.key.lower()) ==
    #             (other.lastname.lower()))
    #
    # def __lt__(self, other):
    #     return ((self.key.lower()) <
    #             (other.key.lower()))

    def get_key(self):
        return self.key

    # Didn't manage to assign (neighbor: Vertice) ass a method parameter
    def add_neighbour(self, neighbor):
        if isinstance(neighbor, Vertice):
            # set(self.neighbors).add(Vertice)
            self.neighbors.append(neighbor) if neighbor not in self.neighbors else self.neighbors
            # set(neighbor.neighbors).add(self)
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
