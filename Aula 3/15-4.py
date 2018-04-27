class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def slope_from_origin(self):
        assert(self.x != 0),"Vertical slope!"
        return self.y/self.x

    def get_line_to(self, p):
        """ if the line is vertical, the error will be raised in the slope function"""
        m = Point(self.x - p.x, self.y - p.y).slope_from_origin()
        c = self.y - m*self.x
        return (m,c)