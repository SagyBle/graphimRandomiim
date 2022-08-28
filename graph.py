from edge import Edge
from vertice import Vertice
import random
from component import Component

import vset_func
import eset_func


class Graph:
    def __init__(self, num_of_vertices: int, edge_set: {Edge}, graph_id: int):
        self.graph_id = graph_id
        ver_set: {Vertice} = set()
        for i in range(0, num_of_vertices):
            ver_set.add(Vertice(i, 0))
        self.vertices = ver_set
        self.edges = edge_set
        self.components: {Component} = set()

    def update_components(self):
        components = set()
        for v in self.vertices:
            components.add(v.component)
        self.components = components

    def create_clique(self):
        edges_tuple_list = []
        for u in self.vertices:
            for v in self.vertices:
                if u.key != v.key and \
                        (u.key, v.key) not in edges_tuple_list and (v.key, u.key) not in edges_tuple_list:
                    edges_tuple_list.append((u.key, v.key))
                    edges_tuple_list.append((v.key, u.key))
                    # print(u.key, v.key)
                    self.edges.add(Edge(u, v))

    def remove_edge(self, e: Edge):
        return self.edges.remove(e)

    # Create random graph, given p = probability for edge to exist has to be
    def create_random_graph(self, p: float):
        if p > 1 or p < 0:
            raise Exception("p has to be in range (0,1)")
        edges_tuple_list = []
        for u in list(self.vertices):
            for v in list(self.vertices):
                if u.key != v.key and \
                        (u.key, v.key) not in edges_tuple_list and (v.key, u.key) not in edges_tuple_list:
                    edges_tuple_list.append((u.key, v.key))
                    edges_tuple_list.append((v.key, u.key))
                    if random.uniform(0, 1) < p:
                        self.edges.add(Edge(u, v))
                        # print(u, v)

    def print_graph(self):
        print("* Graph " + str(self.graph_id) + " *")
        print("Vertices: " + vset_func.vset_to_string(self.vertices))
        print("Edges: " + eset_func.to_string(self.edges))
        print("Components: " + Component.component_set_tostring(self.components))
        # print("Components: ")
        # for c in self.components:
        #     c.to_string()

