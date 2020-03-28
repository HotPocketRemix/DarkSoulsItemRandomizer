class AreaNode():
    def __init__(self, area: str, borders: list[AreaNode], keyitems: dict):
        self.area = area
        self.borders = borders
        self.keyitems = keyitems
