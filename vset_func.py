from vertice import Vertice


def get_num_of_vertices(self):
    return len(self.vertices)


def vset_to_string(vertice_set):
    output = "{"
    for v in vertice_set:
        output = output + str(v.key) + ', '
    return output[:-2] + '}'
