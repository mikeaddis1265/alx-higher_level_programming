class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return

        # Print empty lines based on the position[1] value
        for _ in range(self.position[1]):
            print()

        for i in range(self.size):
            # Print spaces based on the position[0] value
            for _ in range(self.position[0]):
                print(" ", end="")
            # Print '#' characters based on the size
            for _ in range(self.size):
                print("#", end="")
            print()