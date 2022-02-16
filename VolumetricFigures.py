import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from math import pi, cos, sin
import FlatFigures as FlatFigures


class sphere(FlatFigures.Сircle):
    title = 'Сфера'

    def volume_sphere(self):
        return "Объем сферы " + str((4/3) *  np.pi * (self.x ** 3))

    def area_sphere(self):
        return "Площадь сферы " + str(4* np.pi * (self.x ** 2))

    @classmethod
    def output_parameters(cls):
        return ['Введите пожалуйста радиус']


    def draw_sphere(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect('auto')

        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        x = 1 * np.outer(np.cos(u), np.sin(v))
        y = 1 * np.outer(np.sin(u), np.sin(v))
        z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
        elev = 10.0
        rot = 80.0 / 180 * np.pi
        ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)
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


class cube(FlatFigures.Square):
    title = 'Куб'

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону куба']


    def area_cube(self):
        return "Площадь куба " + str(6*self.x**2)
    def volume_cube(self):
        return "Объем куба " + str(self.x ** 3)

    def draw_cube(self):
        axes = [self.x, self.x, self.x]

        data = np.ones(axes, dtype=np.bool)
        alpha = 0.9

        colors = np.empty(axes + [4], dtype=np.float32)

        colors[:] = [1, 0, 0, alpha]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.voxels(data, facecolors=colors)
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

class parallelepiped(FlatFigures.Trapeze):
    title = 'Параллелепипед'

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону Параллелепипеда x','Введите сторону Параллелепипеда y',
                'Введите сторону Параллелепипеда z']


    def area_parallelepiped(self):
        return "Площадь Параллелепипеда " + str(2*(self.x *self.y+self.y*self.h+self.x*self.h))

    def volume_parallelepiped(self):
        return "Объем Параллелепипеда " + str(self.x * self.y +self.h)

    def draw_parallelepiped(self):
        axes = [self.x, self.y, self.h]
        data = np.ones(axes, dtype=np.bool)
        alpha = 0.9
        colors = np.empty(axes + [4], dtype=np.float32)
        colors[:] = [1, 0, 0, alpha]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.voxels(data, facecolors=colors)
        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

class Pyramid(FlatFigures.Square):
    title = 'Пирамида'
    def __init__(self, x , h):
        super().__init__(x)
        self.h = h


    def area_pyramid(self):
        return "Площадь пирамиды " + str(1/2*(self.x * 2) +self.h)

    def volume_pyramid(self):
        return "Объем пирамиды " + str(1/3*(self.x **2) +self.h)

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону пирамиды x','Введите высоту h']


    def draw_pyramid(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = self.x/2
        v = np.array([[-x, -x, -x], [x, -x, -x], [x, x, -x], [-x, x, -x], [0, 0, self.h]])
        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

        verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
                 [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

        ax.add_collection3d(Poly3DCollection(verts,
                                             facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

class cylinder(FlatFigures.Сircle):
    title = 'Цилиндр'
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h


    def area_cylinder(self):
        return "Площадь Цилиндра " + str(2*3.14* self.x *self.h)

    def volume_cylinder(self):
        return "Объем Цилиндра " + str(3.14* self.x*2 *self.h)

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону радиус основания r', 'Введите высоту h']

    def draw_cylinder(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        u = np.linspace(0, 2 * np.pi, 50)
        h = np.linspace(0, self.h, 20)
        x = np.outer(np.sin(u), np.ones(len(h)))
        y = np.outer(np.cos(u), np.ones(len(h)))
        z = np.outer(np.ones(len(u)), h)

        ax.plot_surface(x, y, z,)

        plt.savefig('saved_figure-tight.png', bbox_inches='tight', facecolor='grey')

class cone(cylinder):

    def area_cone(self):
        return "Площадь конуса " + str(2*3.14* self.x *self.h)

    def volume_cone(self):
        return "Объем конуса " + str(3.14* self.x*2 *self.h)

    @classmethod
    def output_parameters(cls):
        return ['Введите сторону радиус основания r', 'Введите высоту h']

    def draw_cone(self):
        z = np.arange(0, self.h, 0.02)
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
