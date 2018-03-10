class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point id={} x={} y={}>".format(self.id, self.x, self.y)

    def __str__(self):
        return "<Point id={} x={} y={}>".format(self.id, self.x, self.y)
