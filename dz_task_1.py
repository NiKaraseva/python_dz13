class MyException(Exception):
    pass

class TriangleSidesException(MyException):
    def __init__(self):
        self.message = f'Invalid size of sides: triangle does not exist'
        super().__init__(self.message)

class SidesLessZeroException(MyException):
    def __init__(self):
        self.message = f'Invalid size of sides: it cannot be less than 0'
        super().__init__(self.message)


class Triangle:
    def __init__(self, side_1: float, side_2: float=None, side_3: float=None):
        self.side_1 = side_1
        if side_2:
            self.side_2 = side_2
        else:
            self.side_2 = side_1
        if side_3:
            self.side_3 = side_3
        else:
            self.side_3 = side_1


    def check_triangle(self):
        if self.side_1 > 0 and self.side_2 > 0 and self.side_3 > 0:
            if self.side_1 + self.side_2 > self.side_3 \
                    or self.side_1 + self.side_3 > self.side_2 \
                    or self.side_2 + self.side_3 > self.side_1:
                if self.side_1 == self.side_2 == self.side_3:
                    return "It's equilateral triangle"
                elif self.side_1 == self.side_2 \
                        or self.side_1 == self.side_3 \
                        or self.side_2 == self.side_3:
                    return "It's isosceles triangle"
                else:
                    return "It's scalene triangle"

            else:
                raise TriangleSidesException()
        else:
            raise SidesLessZeroException()


if __name__ == '__main__':
    tr1 = Triangle(3, 2, 1)
    tr2 = Triangle(-3, 0, 1)

    print(f'tr1 = {tr1.check_triangle()}')
    print(f'tr2 = {tr2.check_triangle()}')

