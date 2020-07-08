
class Polygon:
    """Polygon class creates instance and provide
    all calculation methods to solve equation which needs to
    calculate a polygon"""

    def __init__(self, edges: int, circumradius: int) -> int:
        self._edges = edges
        self._circumradius = circumradius
    
    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self, a):
        if a <= 2:
            raise ValueError(f"Edges amount needs to be higher than {a}")


def main():
    """The main class"""

    # n edges
    n = 4
    # R circumradius
    R = 40

    poly = Polygon(n, R)
    help(Polygon)


if __name__ == "__main__":
    main()
