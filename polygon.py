
class Polygon:
    """Class """

    def __init__(self, edges, circumradius):
        self._edges = edges
        self._circumradius = circumradius


def main():

    # n edges
    n = 4
    # R circumradius
    R = 40

    poly = Polygon(n, R)


if __name__ == "__main__":
    main()
