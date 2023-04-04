class Shapes:
    def __init__(self) -> None:
        pass

    def square(self, ttl, f, choice):
        """
        Makes a square based off of users choice
        """
        if choice:
            for i in range(4):
                ttl.forward(f)
                ttl.left(90)

        else:
            for i in range(4):
                ttl.forward(f)
                ttl.right(90)

    def triangle(self, ttl, f, choice):
        """
        Makes a Triangle from a given choice of direction
        Returns: none
        """
        if choice:
            for i in range(4):
                ttl.forward(f)
                ttl.left(120)
        else:
            for i in range(4):
                ttl.forward(f)
                ttl.right(120)

    # Tiny Snowflake
    def displacement(self, ttl, d):
        """
        This function acts as a transition between drawing
        the next shape. This will turn right. \n
        d = degrees
        """
        ttl.right(d)
        ttl.penup()
        ttl.forward(100)
        ttl.pendown()

    def displacement(self, ttl, d, choice):
        """
        This Method acts as a transition between drawing
        the next shape.  \n
        d = degrees
        """
        if choice:
            ttl.left(d)
            ttl.penup()
            ttl.forward(100)
            ttl.pendown()
        else:
            ttl.right(d)
            ttl.penup()
            ttl.forward(100)
            ttl.pendown()

    def tiny_snowflake(self, ttl, size):
        """
        This Method will create a snowflake where the size
        based on the argument given by the user. \n
        size = turtle size
        """
        for i in range(10):
            ttl.forward(size)
            ttl.right(160)
