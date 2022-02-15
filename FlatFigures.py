from SyperKL import *
import matplotlib.pyplot as plt

class Сircle(GometricFigures):
    title = 'Круг'
    def __init__(self,x):
        super().__init__()
        self.x = x
    def diametr(self):
        return "Диаметр окружности "+str(self.x * 2)


    def areaСircle(self):
        pi = 3.14159
        return "Площадь окружности "+str(pi * (self.x**2))
    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста радиус']
    def printCircle(self):
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


    def areaSquare(self):
        return self.txt+str(self.x **2)

    def perimetrSquare2(self):
        rez = self.x * 4
        return self.txtPr + str(rez)

    def PrintSquare(self):

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([1*self.x, 1*self.x, 2*self.x, 2*self.x, 1*self.x], [1*self.x, 2*self.x, 2*self.x, 1*self.x, 1*self.x])
        # plt.show()
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону квадрата']

class Rectangle(GometricFigures):
    title = 'Прямоугольник'
    def __init__(self, x,y):
        super().__init__()

        self.x = x
        self.y = y


    def areaRectangle(self):
        return "Площадь прямоугольника "+str(self.x * self.y)

    def perimetr(self):
        return "Периметр прямоугольника "+str((self.x + self.y) * 2)

    def PrintRectangle(self):

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([1*self.x, 1*self.x, 2*self.y, 2*self.y, 1*self.x], [1*self.x, 2*self.x, 2*self.x, 1*self.x, 1*self.x])
        # plt.show()
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону прямоугольника x','Введите пожалуйста сторону прямоугольника y']

class Triangle(GometricFigures):
    title = 'Треугольник'
    def __init__(self, a, b, c):
        super().__init__()

        self.a = a
        self.b = b
        self.c = c


    def areaTriangle(self):
        s = (self.a + self.b + self.c) / 2
        return "Площадь треугольника " + str((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5)

    def PrintTriangle(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 1],[1, 2.5, 1, 1])
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

    def perimetr(self):
        return "Периметр треугольника " + str((self.a + self.b + self.c))
    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону треугольника а','Введите пожалуйста сторону треугольника б',
                'Введите пожалуйста сторону треугольника с']

    # 'Введите пожалуйста координаты вершины а пример 1,1',
    # 'Введите пожалуйста координаты вершины б пример 2,2.5', 'Введите пожалуйста координаты вершины с пример 3,1'
class Trapeze(GometricFigures):
    title = 'Трапеция'
    def __init__(self, x, y, b, a,h):
        super().__init__()

        self.x = x
        self.y = y
        self.h = h
        self.a = a
        self.b = b


    def areaTrapeze(self):
        return "площадь трапеции " + str(1/2*self.h*(self.x + self.y))
    def perimetr(self):
        return "Периметр трапеции " + str(self.x + self.y+self.a+self.b)
    def PrintTrapeze(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([0.3, 0.6, 0.5, 0.4, 0.3], [0.7, 0.7, 0.9, 0.9, 0.7])
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону трапеции x', 'Введите пожалуйста сторону трапеции y',
                'Введите пожалуйста сторону трапеции a','Введите пожалуйста сторону трапеции b',
                'Введите пожалуйста высоту трапеции h']
class Rhombus(Square):
    title = 'Ромб'

    def area_Rhombus(self):
        self.txt = "Площадь ромба "
        return self.area()

    def perimetr_Rhombus(self):
        self.txtPr = "Периметр ромба "
        return self.perimetrSquare2()

    @staticmethod
    def output_parameters():
        return ['Введите пожалуйста сторону ромба x']

    def PrintRhombus(self):

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot([0.3, 0.6, 0.9, 0.6 , 0.3], [0.25, 0.45, 0.25, 0.05, 0.25])
        plt.axis('scaled')
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')