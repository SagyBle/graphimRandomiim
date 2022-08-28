import random
from graph import Graph
from edge import Edge
from vertice import Vertice

if __name__ == '__main__':

    # Constants assignments.
    NUMBER_OF_VERTICES = 10
    GRAPH_ID = 0
    EDGE_EXISTENCE_PROBABILITY = 0.1

    graph0 = Graph(NUMBER_OF_VERTICES, GRAPH_ID)

    # Create random graph, means "flip a coin" whether edge (u,v) appear in the graph in EDGE_EXISTENCE_PROBABILITY
    # probability ,for all (u,v) in G, so that u,v are numbers in range (0, NUMBER_OF_VERTICES) and u != v.
    graph0.create_random_graph(EDGE_EXISTENCE_PROBABILITY)

    # Get updated components according to edges added.
    graph0.update_components()

    graph0.print_graph()
