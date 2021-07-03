class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        a = self.point1.dist_to(self.point2)
        b = self.point1.dist_to(self.point3)
        c = self.point2.dist_to(self.point3)

        return a + b + c

    def area(self):
        a = self.point1.dist_to(self.point2)
        b = self.point1.dist_to(self.point3)
        c = self.point2.dist_to(self.point3)

        hp = (a + b + c) / 2

        return (hp * (hp - a) * (hp - b) * (hp - c)) ** 0.5


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(6, 8), Point(2, 2))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

per = triangle1.perimeter()
area = triangle1.area()

print("Периметр треугольника = ", per)
print("Площадь треугольника = ", area)
