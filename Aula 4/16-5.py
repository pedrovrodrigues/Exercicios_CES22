class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height
    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

def detect_collision(r1, r2):
    if r1.corner.x + r1.width <= r2.corner.x:
        if r1.corner.y - r1.height <= r2.corner.y
            return True
        if r2.corner.y - r2.height <= r1.corner.y
            return True
    if r2.corner.x + r2.width <= r1.corner:
        if r1.corner.y - r1.height <= r2.corner.y
            return True
        if r2.corner.y - r2.height <= r1.corner.y
            return True
    return False