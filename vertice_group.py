from vertice import Vertice


class VerticeGroup:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.vertices = list()
        for i in range(0, num_of_vertices):
            self.vertices.append(Vertice(i, 0))

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice):
            self.vertices.append(vertice)
        else:
            raise Exception("Only Vertice's instances may be added to VerticeGroup")

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice):
            self.vertice.append(vertice)
        else:
            raise Exception("Only Vertice's instances may be added to VerticeGroup")

