import math


class ManyPolygons:
    """
    ManyPolygon class calls the Polygon class and creates many polygons as needed.
    """

    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]

    def __repr__(self):
        return f"Polygon(n={self._m},R={self._R})"

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area/p.perimeter, reverse=True)
        return sorted_polygons[0]


class Polygon:
    """
    Polygon class creates instance and provide
    all calculation methods to solve equation which needs to
    calculate a polygon. The Polygon class will create an instance using these parameters 
    * n edges(=n vertices)
    * R circumradius
    """

    def __init__(self, n: int, R: int):
        self._n = n
        self._R = R

    @property
    def edges(self):
        return self._n

    @edges.setter
    def edges(self, n):
        if n <= 2:
            raise ValueError("ERROR! ns amount needs to be higher than 2")
        elif not isinstance(n, int):
            raise ValueError("ERROR! variable n is not integer")
        else:
            self._n = n

    @property
    def circumradius(self):
        return self._R

    @circumradius.setter
    def circumradius(self, R):
        if R < 1:
            raise ValueError("ERROR! R needs to be higher than 1")
        elif not isinstance(R, int):
            raise ValueError("ERROR! variable R is not integer")
        else:
            self._R = R

    @property
    def interior_angle(self):
        return(self.edges-2) * 180 / self.edges

    @property
    def s_edge_lenght(self):
        return 2 * self.circumradius * math.sin(math.pi/self.edges)

    @property
    def a_apothem(self):
        return self.circumradius * math.cos(math.pi/self.edges)

    @property
    def area(self):
        return self.edges / 2 * self.s_edge_lenght * self.a_apothem

    @property
    def perimeter(self):
        return self.edges * self.s_edge_lenght

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.circumradius == other.circumradius and self.edges == other.edges
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.edges > other.edges
        else:
            return NotImplemented

    def __str__(self):
        return "Polygon(n={0}, R={1})".format(self.edges, self.circumradius)


def main():
    """The main class"""
    pp = ManyPolygons(3, 4)
    # Prints the Polygon with the highest area : perimeter ratio
    print(pp.max_efficiency_polygon)
    # Prints all
    ([(print(p), print(p.area/p.perimeter)) for p in pp])


def test_polygon():
    """
    The test class, which includes 2 separate tests that all changes are correct in the code.
    The class use relative and absolute tolerances set up 0.001 accuracy.
    """
    # Relative tolerance
    rel_tol = 0.001
    # Absolute tolerance level
    abs_tol = 0.001

    # Test number 1
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == f"Polygon(n=3, R=1)", f"actual-->  {str(p)}"
    assert p.edges == n, f"actual: {p.edges}"
    assert p.circumradius == R, f"actual: {p.circumradius}"
    assert p.interior_angle == 60, f"actual: {p.circumradius}"

    # Test number 2
    n = 4
    R = 1
    p = Polygon(n, R)

    assert str(p) == f"Polygon(n=4, R=1)", f"actual-->  {str(p)}"
    assert p.edges == n, f"actual: {p.edges}"
    assert p.circumradius == R, f"actual: {p.circumradius}"
    assert math.isclose(p.interior_angle, 90,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)
    assert math.isclose(p.area, 2.0,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f"actual: {p.area}, "
                                           f" expected: {2.0}")

    assert math.isclose(p.perimeter, 4*math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    assert math.isclose(p.a_apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    # Test number 3
    n = 6
    R = 2
    p = Polygon(n, R)

    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f"actual: {p.area}, "
                                           f" expected: {10.3923}")

    assert math.isclose(p.s_edge_lenght, 2,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    assert math.isclose(p.a_apothem, 1.73205,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    # Test number 4
    n = 12
    R = 3
    p = Polygon(n, R)

    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f"actual: {p.area}, "
                                           f" expected: {10.3923}")

    assert math.isclose(p.s_edge_lenght, 1.55291,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    assert math.isclose(p.a_apothem, 2.89778,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    # Test objects initialization
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    # Test number 5
    assert p2 > p1

    # Test number 6
    assert p2 < p3

    # Test number 7
    assert p3 != p4

    # Test number 8
    assert p1 != p4

    # Test number 9
    assert p4 == p5


if __name__ == "__main__":
    test_polygon()
    main()
