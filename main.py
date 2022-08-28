import random
from graph import Graph
from edge import Edge
from vertice import Vertice

if __name__ == '__main__':

    graph0 = Graph(9, set(), 0)
    graph0.create_random_graph(0.2)
    graph0.update_components()
    graph0.print_graph()

    print("compiled")

