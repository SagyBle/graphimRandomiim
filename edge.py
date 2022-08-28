import graph
from vertice import Vertice
from component import Component


class Edge:
    def __init__(self, ver1: Vertice, ver2: Vertice):
        # Keeping the smaller key first.
        if ver1.key >= 0 and ver2.key >= 0:
            if ver1.key < ver2.key:
                self.edge = (ver1, ver2)
                self.ver1 = ver1
                self.ver2 = ver2
            elif ver2.key < ver1.key:
                self.edge = (ver2, ver1)
                self.ver1 = ver2
                self.ver2 = ver1
            else:
                raise Exception("ver1 and ver2 have to be different")

        # For edge created (ver1, ver2), update both vertices neighbours sets.
        ver1.add_neighbour(ver2)

        # Get and merge both components to a unified one, and assign it to be the new
        # component of ver1, ver2, and all neighbours of ver1 and ver2.
        c1 = self.ver1.component.vertices
        c2 = self.ver2.component.vertices
        unified_c1c2_vertices = c1.union(c2)
        unified_c1c2_component = Component(unified_c1c2_vertices)

        for v in unified_c1c2_vertices:
            v.component = unified_c1c2_component


    def print_edge(self):
        print(self.edge)

    def tostring(self) -> str:
        return "(" + str(self.ver1.key) + ", " + str(self.ver2.key) + ")"

    def unify_components(self):
        c1 = self.ver1.component.vertices
        c2 = self.ver2.component.vertices
        unified_c1c2 = c1.union(c2)
        self.ver1.component.vertices = unified_c1c2
        self.ver2.component = self.ver1.component





