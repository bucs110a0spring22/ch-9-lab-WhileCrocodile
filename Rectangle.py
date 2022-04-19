class Rectangle:
  def __init__(self, x, y, h, w):
    '''
    Initializes the Rectangle object.
    x: (int) x coordinate of the top left of the rectangle
    y: (int) y coordinate of the top left of the rectangle
    h: (int) height of the rectangle
    w: (int) width of the rectangle
    '''
    init_vars = [0 if var < 0 else var for var in [x, y, h, w]]
    self.x = init_vars[0]
    self.y = init_vars[1]
    self.height = init_vars[2]
    self.width = init_vars[3]

  def __str__(self):
    '''
    Returns the x coordinate, y coordinate, height and width of the Rectangle as a string.
    return: (str) x, y, height and width of the rectangle.
    '''
    return f"x: {self.x}, y: {self.y}, height: {self.height}, width: {self.width}"
  