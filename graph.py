from edge import Edge
from vertice import Vertice
import random
from component import Component

import vset_func
import eset_func


class Graph:
    def __init__(self, num_of_vertices: int, graph_id: int):
        self.graph_id = graph_id
        ver_set: {Vertice} = set()
        for i in range(0, num_of_vertices):
            ver_set.add(Vertice(i, 0))
        self.vertices = ver_set
        self.edges = set()
        self.components: {Component} = set()

    # After adding edges to the graph, use update_components() to go get the update components.
    def update_components(self):
        components = set()
        for v in self.vertices:
            components.add(v.component)
        self.components = components

    # Creates clique out of empty edges set graph.
    def create_clique(self):
        tested_edges_tuple_list = []
        # for all u,v in V, s.t: u != v, add (u,v) to E.
        for u in self.vertices:
            for v in self.vertices:
                # If keys are different, and (u,v) has not been tested as (v,u) before.
                if u.key != v.key and \
                        (u.key, v.key) not in tested_edges_tuple_list and (v.key, u.key) not in tested_edges_tuple_list:
                    # Add (u,v) and (v,u) to list of edges that have been added.
                    tested_edges_tuple_list.append((u.key, v.key))
                    tested_edges_tuple_list.append((v.key, u.key))
                    self.edges.add(Edge(u, v))

    def remove_edge(self, e: Edge):
        return self.edges.remove(e)

    # Create a random graph, out of complete graph.
    # Remove an edge e, in a probability of 1-p.
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

    def print_graph(self):
        print("* Graph " + str(self.graph_id) + " *")
        print("Vertices: " + vset_func.vset_to_string(self.vertices))
        print("Edges: " + eset_func.to_string(self.edges))
        print("Components: " + Component.component_set_tostring(self.components))

