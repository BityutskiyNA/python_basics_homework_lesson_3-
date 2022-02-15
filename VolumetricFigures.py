from SyperKL import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from math import pi, cos, sin


class sphere(GometricFigures):
    title = 'Сфера'
    def __init__(self,x):
        super().__init__()
        self.x = x
    def obem(self):
        pi = 3.14159
        return "Объем сферы " + str((4/3) * pi * (self.x ** 3))


    def areasphere(self):
        pi = 3.14159
        return "Площадь сферы " + str(4*pi * (self.x ** 2))
    @classmethod
    def output_parameters(cls):
        return ['Введите пожалуйста радиус']
    def PrintSphere(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect('auto')

        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        x = 1 * np.outer(np.cos(u), np.sin(v))
        y = 1 * np.outer(np.sin(u), np.sin(v))
        z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
        # for i in range(2):
        #    ax.plot_surface(x+random.randint(-5,5), y+random.randint(-5,5), z+random.randint(-5,5),  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)
        elev = 10.0
        rot = 80.0 / 180 * np.pi
        ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)
        # calculate vectors for "vertical" circle
        a = np.array([-np.sin(elev / 180 * np.pi), 0, np.cos(elev / 180 * np.pi)])
        b = np.array([0, 1, 0])
        b = b * np.cos(rot) + np.cross(a, b) * np.sin(rot) + a * np.dot(a, b) * (1 - np.cos(rot))
        ax.plot(np.sin(u), np.cos(u), 0, color='k', linestyle='dashed')
        horiz_front = np.linspace(0, np.pi, 100)
        ax.plot(np.sin(horiz_front), np.cos(horiz_front), 0, color='k')
        vert_front = np.linspace(np.pi / 2, 3 * np.pi / 2, 100)
        ax.plot(a[0] * np.sin(u) + b[0] * np.cos(u), b[1] * np.cos(u), a[2] * np.sin(u) + b[2] * np.cos(u), color='k',
                linestyle='dashed')
        ax.plot(a[0] * np.sin(vert_front) + b[0] * np.cos(vert_front), b[1] * np.cos(vert_front),
                a[2] * np.sin(vert_front) + b[2] * np.cos(vert_front), color='k')

        ax.view_init(elev=elev, azim=0)

        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')



class cube(GometricFigures):
    title = 'Куб'
    def __init__(self, x):
        super().__init__()
        self.x = x

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону куба']


    def areacube(self):
        return "Площадь куба " + str(6*self.x**2)
    def volume(self):
        return "Объем куба " + str(self.x ** 3)

    def PrintСube(self):
        # Create axis
        axes = [self.x, self.x, self.x]

        data = np.ones(axes, dtype=np.bool)
        alpha = 0.9

        colors = np.empty(axes + [4], dtype=np.float32)

        colors[:] = [1, 0, 0, alpha]  # red

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.voxels(data, facecolors=colors)
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

class parallelepiped(GometricFigures):
    title = 'Параллелепипед'
    def __init__(self, x, y, z):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону Параллелепипеда x','Введите сторону Параллелепипеда y',
                'Введите сторону Параллелепипеда z']


    def areaparallelepiped(self):
        return "Площадь Параллелепипеда " + str(2*(self.x *self.y+self.y*self.z+self.x*self.z))

    def volume(self):
        return "Объем Параллелепипеда " + str(self.x * self.y +self.z)

    def Printparallelepiped(self):
        # Create axis
        axes = [self.x, self.y, self.z]

        data = np.ones(axes, dtype=np.bool)
        alpha = 0.9

        colors = np.empty(axes + [4], dtype=np.float32)

        colors[:] = [1, 0, 0, alpha]  # red

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.voxels(data, facecolors=colors)
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

class Pyramid(GometricFigures):
    title = 'Пирамида'
    def __init__(self, x , y, h):
        super().__init__()

        self.x = x
        self.y = y
        self.h = h


    def areaPyramid(self):
        return "Площадь пирамиды " + str(1/2*(self.x + self.y) +self.h)

    def volume(self):
        return "Объем пирамиды " + str(1/3*(self.x * self.y) +self.h)

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону пирамиды x','Введите сторону пирамиды y',
                'Введите высоту h']


    def PrintPyramid(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # vertices of a pyramid
        v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [0, 0, 1]])
        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

        # generate list of sides' polygons of our pyramid
        verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
                 [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

        # plot sides
        ax.add_collection3d(Poly3DCollection(verts,
                                             facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

class cylinder(GometricFigures):
    title = 'Цилиндр'
    def __init__(self, r, h):
        super().__init__()
        self.r = r
        self.h = h


    def areacylinder(self):
        return "Площадь Цилиндра " + str(2*3.14* self.r *self.h)

    def volume(self):
        return "Объем Цилиндра " + str(3.14* self.r*2 *self.h)

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону радиус основания r', 'Введите высоту h']

    def Printparallelepiped(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        u = np.linspace(0, 2 * np.pi, 50)
        h = np.linspace(0, 1, 20)
        x = np.outer(np.sin(u), np.ones(len(h)))
        y = np.outer(np.cos(u), np.ones(len(h)))
        z = np.outer(np.ones(len(u)), h)

    # Plot the surface
        ax.plot_surface(x, y, z,)

        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')
class cone(GometricFigures):
    def __init__(self, r, h):
        super().__init__()
        self.r = r
        self.h = h


    def areacone(self):
        return "Площадь конуса " + str(2*3.14* self.r *self.h)

    def volume(self):
        return "Объем конуса " + str(3.14* self.r*2 *self.h)

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону радиус основания r', 'Введите высоту h']

    def Printcone(self):
        z = np.arange(0, 1, 0.02)
        theta = np.arange(0, 2 * pi + pi / 50, pi / 50)

        fig = plt.figure()
        axes1 = fig.add_subplot(111, projection='3d')
        for zval in z:
            x = zval * np.array([cos(q) for q in theta])
            y = zval * np.array([sin(q) for q in theta])
            axes1.plot(x, y, -zval, 'b-')
        axes1.set_xlabel("x label")
        axes1.set_ylabel("y label")
        axes1.set_zlabel("z label")

        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')
