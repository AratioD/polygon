import math


class Polygon:
    """Polygon class creates instance and provide
    all calculation methods to solve equation which needs to
    calculate a polygon. The Polygon class will create an instance using these parameters 
    * n edges(=n vertices)
    * R circumradius"""

    def __init__(self, n: int, R: int) -> int:
        self.n = n
        self.R = R

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        if n <= 2:
            raise ValueError("ERROR! ns amount needs to be higher than 2")
        elif not isinstance(n, int):
            raise ValueError("ERROR! variable n is not integer")
        else:
            self._n = n

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, R):
        if R < 1:
            raise ValueError("ERROR! R needs to be higher than 1")
        elif not isinstance(R, int):
            raise ValueError("ERROR! variable R is not integer")
        else:
            self._R = R

    @property
    def interior_angle(self):
        return(self.n-2) * 180 / self.n

    @property
    def s_edge_lenght(self):
        return 2 * self.R * math.sin(math.pi/self.n)

    @property
    def a_apothem(self):
        return self.R * math.cos(math.pi/self.n)

    @property
    def area(self):
        return 1/2 * self.n * self.s_edge_lenght * self.a_apothem

    @property
    def perimeter(self):
        return self.n * self.s_edge_lenght

    def __repr__(self):
        return "ns and R({0}, {1})".format(self.R, self.n)

    # def __eq__(self, other):
    #     return self.n == other.ns and self.R == other

    def __str__(self):
        return "Polygon, R--> {0}, ns--> {1}".format(self.R, self.n)


def main():
    """The main class"""
    polygons = {(4, 7877), (4, 5), (5, 4), (7, 8), (23, 34),
                (545, 5656), (3, 3), (4, 4), (6, 6)}
    poly_list = []
    # print(type(polygons))
    # # n ns
    # n = 4
    # # R R
    # R = 40

    # help(Polygon)
    for i in polygons:
        poly_list.append(Polygon(i[0], i[1]))

    # Print all variables
    for k in poly_list:
        print(k)

        print("interior angle -->", k.interior_angle, " edge lenght -->",
              k.s_edge_lenght, " apothem -->", k.a_apothem, " area -->", k.area, " perimeter--> ", k.perimeter)


if __name__ == "__main__":
    main()
