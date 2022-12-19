

class Plane:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.size = 50;
        self.position = [400, 700]

    def __str__(self) -> str:
        return self.name
