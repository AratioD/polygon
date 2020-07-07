
class Polygon:
    """Polygon class creates instance and calculate a polygon"""

    def __init__(self, edges: int, circumradius: int) -> int:
        self._edges = edges
        self._circumradius = circumradius


def main():

    # n edges
    n = 4
    # R circumradius
    R = 40

    poly = Polygon(n, R)
    help(Polygon)


if __name__ == "__main__":
    main()
