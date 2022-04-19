from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    '''
    Initializes the Surface object, composed of an image and a Rectangle object.
    filename: (str) path to the image file
    x: (int) x coordinate of the top left of the rectangle
    y: (int) y coordinate of the top left of the rectangle
    h: (int) height of the rectangle
    w: (int) width of the rectangle
    '''
    self.rect = Rectangle(x, y, h, w)
    self.image = filename

  def getRect(self):
    '''
    Returns the internal Rectangle object.
    return: (Rectangle) The internal rectangle object
    '''
    return self.rect