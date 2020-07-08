
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
        
    @property
    def circumradius(self):
        return self._circumradius
    
    @circumradius.setter
    def circumradius(self, a):
        if a < 1:
            raise ValueError(f"Circumradius needs to be higher than 1")
        




def main():
    """The main class"""

    # n edges
    n = 4
    # R circumradius
    R = 40

    poly = Polygon(n, R)
    # help(Polygon)
    
    #test
    poly.circumradius = 1.2
    poly.edges = 2
    
    


if __name__ == "__main__":
    main()
