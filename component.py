class Component:
    def __init__(self, vertice_set):
        if isinstance(vertice_set, set):
            self.vertices = vertice_set
        else:
            raise Exception("vertice set has to be set of vertices")
        # not sure if necessary
        # self.id = vertice.key

    def add_vertices_to_component(self, component_set):
        if isinstance(component_set, set):
            self.vertices.union(component_set)

    def to_string(self):
        if len(self.vertices) == 0:
            return "{}"
        output = "{"
        for v in self.vertices:
            output = output + str(v.key) + ', '
        return output[:-2] + '}'

    def print_component(self):
        print(self.to_string())

    def component_set_tostring(component_set):
        if len(component_set) == 0:
            return "{}"
        output = "{"
        for c in component_set:
            output += c.to_string() + ", "
        return output[:-2] + '}'

    def get_component_size(self) -> int:
        return len(self.vertices)
