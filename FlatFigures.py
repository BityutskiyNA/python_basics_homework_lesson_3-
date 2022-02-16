import matplotlib.pyplot as plt
import numpy as np


class GometricFigures():
    title = 'Фигура'

    def area(self):
        pass

    def return_data(self):
        pass


class Сircle(GometricFigures):
    title = 'Круг'

    def __init__(self, x):
        super().__init__()
        self.x = x

    def diametr(self):
        return "Диаметр окружности " + str(self.x * 2)

    def area_circle(self):
        return "Площадь окружности " + str(np.pi * (self.x ** 2))

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста радиус']

    def draw_circle(self):
        circle1 = plt.Circle((1, 1), self.x, color='b', fill=True)
        ax = plt.gca()
        ax.add_patch(circle1)
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')


class Square(GometricFigures):
    title = 'Квадрат'

    def __init__(self, x):
        super().__init__()
        self.x = x
        self.txt = "Площадь квадрата "
        self.txtPr = "Периметр квадрата "

    def area_square(self):
        return self.txt + str(self.x ** 2)

    def perimetr_square2(self):
        rez = self.x * 4
        return self.txtPr + str(rez)

    def draw_square(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([1 * self.x, 1 * self.x, 2 * self.x, 2 * self.x, 1 * self.x],
                [1 * self.x, 2 * self.x, 2 * self.x, 1 * self.x, 1 * self.x])
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону квадрата']


class Rectangle(Square):
    title = 'Прямоугольник'

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area_rectangle(self):
        return "Площадь прямоугольника " + str(self.x * self.y)

    def perimetr(self):
        return "Периметр прямоугольника " + str((self.x + self.y) * 2)

    def draw_rectangle(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([1 * self.x, 1 * self.x, 2 * self.y, 2 * self.y, 1 * self.x],
                [1 * self.x, 2 * self.x, 2 * self.x, 1 * self.x, 1 * self.x])
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону прямоугольника x', 'Введите пожалуйста сторону прямоугольника y']


class Triangle(GometricFigures):
    title = 'Треугольник'

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area_triangle(self):
        s = (self.a + self.b + self.c) / 2
        rez = str((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5)
        return "Площадь треугольника {a} см2 ".format(a = rez)

    def calc_angles(self, a, b, c):
        alpha = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2. * b * c))
        beta = np.arccos((-b ** 2 + c ** 2 + a ** 2) / (2. * a * c))
        gamma = np.pi - alpha - beta
        return alpha, beta, gamma

    def calc_point(self, alpha, beta, c):
        x = (c * np.tan(beta)) / (np.tan(alpha) + np.tan(beta))
        y = x * np.tan(alpha)
        return (x, y)

    def get_triangle(self, a, b, c):
        z = np.array([a, b, c])
        while z[-1] != z.max():
            z = z[[2, 0, 1]]
        alpha, beta, _ = self.calc_angles(*z)
        x, y = self.calc_point(alpha, beta, z[-1])
        return [(0, 0), (z[-1], 0), (x, y)]

    def draw_triangle(self):
        fig, ax = plt.subplots()
        ax.set_aspect("equal")

        dreieck = plt.Polygon(self.get_triangle(self.a, self.b, self.c))
        ax.add_patch(dreieck)
        ax.relim()
        ax.autoscale_view()
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

    def perimetr(self):
        rez= str((self.a + self.b + self.c))
        return "Периметр треугольника {a} см.".format(a = rez)

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону треугольника а', 'Введите пожалуйста сторону треугольника б',
                'Введите пожалуйста сторону треугольника с']


class Trapeze(Rectangle):
    title = 'Трапеция'

    def __init__(self, x, y, h):
        super().__init__(x, y)
        self.h = h

    def area_trapeze(self):
        return "Площадь трапеции " + str(1 / 2 * self.h * (self.x + self.y))

    def perimetr(self):
        return "Периметр трапеции " + str(self.x + self.y)

    def draw_trapeze(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([3, 10 + self.y, 8 + self.x, 5, 3],
                [7, 7, 9, 9, 7])
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону трапеции x', 'Введите пожалуйста сторону трапеции y',
                'Введите пожалуйста высоту трапеции h']


class Rhombus(Square):
    title = 'Ромб'

    def area_rhombus(self):
        self.txt = "Площадь ромба "
        return self.area_square()

    def perimetr_rhombus(self):
        self.txtPr = "Периметр ромба "
        return self.perimetr_square2()

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону ромба x']

    def draw_rhombus(self):

        t = np.arange(0, 360 + (360 / 4), 360 / 4)
        x = self.x * np.sin(np.radians(t))
        y = self.x * np.cos(np.radians(t))

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        # plt.plot(x, y)
        plt.axis('equal')
        elev = 10.0
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')
