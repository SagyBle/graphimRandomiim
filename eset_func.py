from edge import Edge


def to_string(e_set: {Edge}):
    if len(e_set) == 0:
        return "{}"
    output = "{"
    for e in e_set:
        output = output + (e.tostring()) + ', '

    return output[:-2] + "}"





def print_edge_group(e_set):
    print(e_set.to_string())
