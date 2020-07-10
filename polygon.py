
class Polygon:
    """Polygon class creates instance and provide
    all calculation methods to solve equation which needs to
    calculate a polygon"""

    def __init__(self, edge: int, circumradius: int) -> int:
        self._edge = edge
        self._circumradius = circumradius

    @property
    def edge(self):
        return self._edge

    @edge.setter
    def edge(self, edge):
        if edge <= 2:
            raise ValueError("Edges amount needs to be higher than 2")
        else:
            self._edge = edge

    @property
    def circumradius(self):
        return self._circumradius

    @circumradius.setter
    def circumradius(self, circumradius):
        if circumradius < 1:
            raise ValueError("Circumradius needs to be higher than 1")
        else:
            self._circumradius = circumradius

    def __repr__(self):
        return "Edges and circumradius({0}, {1})".format(self._edge, self._circumradius)

    def __eq__(self, other):
        return self._edge == other.edges and self._circumradius == other

    def __str__(self):
        return "Polygon, cirumradius--> {0}, edges--> {1}".format(self._circumradius, self._edge)


def main():
    """The main class"""
    polygons = {(2, 3), (5, 4), (7, 8), (23, 34),
                (545, 5656), (3, 3), (4, 4), (6, 6)}
    poly_list = []
    print(type(polygons))
    # n edges
    n = 4
    # R circumradius
    R = 40

    for i in polygons:
        poly_list.append(Polygon(i[0], i[1]))

    # Print all variables
    for k in poly_list:
        print(k)


if __name__ == "__main__":
    main()
