from tkinter import *
from tkinter import ttk
import FlatFigures as FlatFigures
import VolumetricFigures as VolumetricFigures

window = Tk()
vidgets = []
params = []

def calculate_cm():
    """Функция нажатия кнопки calculate, в зависимости от значения списка вызываются методы классов и создаются
    соотвестующие  экзепляры класса в параметры передаются элементы массива params"""

    mass_rez =[]
    if lis.get() == 'Круг':
         circle_obj = FlatFigures.Сircle(int(params[0].get()))
         area = circle_obj.area_circle()
         diametr = circle_obj.diametr()
         mass_rez =[area, diametr]
         circle_obj.draw_circle()
    elif lis.get() == 'Квадрат':
         square_obj = FlatFigures.Square(int(params[0].get()))
         area = square_obj.area_square()
         perimeter = square_obj.perimetr_square2()
         mass_rez = [area,perimeter]
         square_obj.draw_square()
    elif lis.get() == 'Прямоугольник':
         rectangle_obj = FlatFigures.Rectangle(int(params[0].get()), int(params[1].get()))
         area = rectangle_obj.area_rectangle()
         perimeter = rectangle_obj.perimetr()
         mass_rez = [area, perimeter]
         rectangle_obj.draw_rectangle()
    elif lis.get() == 'Треугольник':
         triangle_obj = FlatFigures.Triangle(int(params[0].get()), int(params[1].get()),int(params[2].get()))
         area = triangle_obj.area_triangle()
         perimeter = triangle_obj.perimetr()
         mass_rez = [area, perimeter]
         triangle_obj.draw_triangle()
    elif lis.get() == 'Трапеция':
         Trapeze_obj = FlatFigures.Trapeze(int(params[0].get()),int(params[1].get()),int(params[2].get()))
         area = Trapeze_obj.area_trapeze()
         perimeter = Trapeze_obj.perimetr()
         mass_rez = [area, perimeter]
         Trapeze_obj.draw_trapeze()
    elif lis.get() == 'Ромб':
         Rhombus_obj = FlatFigures.Rhombus(int(params[0].get()))
         area = Rhombus_obj.area_rhombus()
         perimeter = Rhombus_obj.perimetr_rhombus()
         mass_rez = [area, perimeter]
         Rhombus_obj.draw_rhombus()
    elif lis.get() == 'Сфера':
         sphere_obj = VolumetricFigures.sphere(int(params[0].get()))
         area = sphere_obj.volume_sphere()
         diametr = sphere_obj.volume_sphere()
         mass_rez = [area, diametr]
         sphere_obj.draw_sphere()
    elif lis.get() == 'Куб':
         cube_obj = VolumetricFigures.cube(int(params[0].get()))
         area = cube_obj.area_cube()
         volume = cube_obj.volume_cube()
         mass_rez = [area, volume]
         cube_obj.draw_cube()
    elif lis.get() == 'Параллелепипед':
         parallelepiped_obj = VolumetricFigures.parallelepiped(int(params[0].get()), int(params[1].get()), int(params[2].get()))
         area = parallelepiped_obj.area_parallelepiped()
         volume = parallelepiped_obj.volume_parallelepiped()
         mass_rez = [area, volume]
         parallelepiped_obj.draw_parallelepiped()
    elif lis.get() == 'Пирамида':
         Pyramid_obj = VolumetricFigures.Pyramid(int(params[0].get()), int(params[1].get()))
         area = Pyramid_obj.area_pyramid()
         volume = Pyramid_obj.volume_pyramid()
         mass_rez = [area, volume]
         Pyramid_obj.draw_pyramid()
    elif lis.get() == 'Цилиндр':
         cylinder_obj = VolumetricFigures.cylinder(int(params[0].get()), int(params[1].get()))
         area = cylinder_obj.area_cylinder()
         volume = cylinder_obj.volume_cylinder()
         mass_rez = [area, volume]
         cylinder_obj.draw_cylinder()
    elif lis.get() == 'Конус':
         cone_obj = VolumetricFigures.cone(int(params[0].get()), int(params[1].get()))
         area = cone_obj.area_cone()
         volume = cone_obj.volume_cone()
         mass_rez = [area, volume]
         cone_obj.draw_cone()
    output_result(mass_rez, len(params) * 20 + 30)

def output_result(mass_rez,vert):
    """Функция выводит результат расчетов на форму
            входящие параметры: mass_rez - массив результтат
                                vert - растояние в пикселях от которого начинаем рисовать на форме результат"""
    vert + 30
    for i in mass_rez:
        lbl = Label(window, text=i)
        lbl.place(x=0, y=vert)
        vert = vert+20
        vidgets.append(lbl)

def draw_cm():
    """Функция выводит изображение с отрисованой фигурой на форму """
    blank_drawing()
    our_image = PhotoImage(file="saved_figure-tight.png")
    width_our_image = our_image.width()
    if width_our_image > 800:
        our_image = our_image.subsample(2, 2)
    our_label = Label(window)
    our_label.image = our_image
    our_label['image'] = our_label.image
    our_label.place(x=300, y=0)

def clear_cm():
    """Функция очищает форму от элементов параметров фигуры и результатов вычислений """
    blank_drawing()
    for i in vidgets:
        i.destroy()
    for i in params:
        i.destroy()

def event_handling(nameobg):
    """Функция получает параметры из методов класса в зависимости от значения  nameobg"""
    clear_cm()
    x = 200
    parameter_list = []
    if nameobg == 'Круг':
        parameter_list = FlatFigures.Сircle.output_parameters()
        x = 160
    elif nameobg == 'Квадрат':
        parameter_list = FlatFigures.Square.output_parameters()
        x = 230
    elif nameobg == 'Прямоугольник':
        parameter_list = FlatFigures.Rectangle.output_parameters()
        x = 260
    elif nameobg == 'Треугольник':
        parameter_list = FlatFigures.Triangle.output_parameters()
        x = 260
    elif nameobg == 'Сфера':
        parameter_list = VolumetricFigures.sphere.output_parameters()
        x = 160
    elif nameobg == 'Куб':
        parameter_list = VolumetricFigures.cube.output_parameters()
        x = 160
    elif nameobg == 'Параллелепипед':
        parameter_list = VolumetricFigures.parallelepiped.output_parameters()
        x = 200
    elif nameobg == 'Пирамида':
        parameter_list = VolumetricFigures.Pyramid.output_parameters()
        x = 200
    elif nameobg == 'Цилиндр':
        parameter_list = VolumetricFigures.cylinder.output_parameters()
        x = 200
    elif nameobg == 'Конус':
        parameter_list = VolumetricFigures.cone.output_parameters()
        x = 200
    elif nameobg == 'Трапеция':
        parameter_list  = FlatFigures.Trapeze.output_parameters()
        x = 240
    elif nameobg == 'Ромб':
        parameter_list = FlatFigures.Rhombus.output_parameters()
        x = 220
    fill_parameters(parameter_list, x)
def fill_parameters (ParamList,gor):
    """Функция выводит на форму параметры
            входящие параметры: ParamList - массив параметров
                                gor - растояние в пикселях от которого начинаем рисовать на форме результат"""
    vert = 30
    params.clear()
    for x in ParamList:
        lbl = Label(window, text=x)
        lbl.place(x=0, y=vert)
        param = Entry(window, width=10)
        param.place(x=gor, y=vert)
        vidgets.append(lbl)
        params.append(param)
        vert = vert + 20

def callbackFunc(event):
    event_handling(lis.get())

def blank_drawing ():
    """Функция выводит пустое изображение на форму закрасить предыдущий рисунок"""
    our_image = PhotoImage(file="background.png")
    our_image = our_image.subsample(1, 1)
    our_label = Label(window)
    our_label.image = our_image
    our_label['image'] = our_label.image
    our_label.place(x=300, y=0)

if __name__ == '__main__':
    window.title("Геометрический калькулятор")
    window.geometry('1000x410')
    selected = IntVar()

    r = ['Круг', 'Квадрат', 'Прямоугольник', 'Треугольник', 'Трапеция', 'Ромб', 'Сфера'
        , 'Куб', 'Параллелепипед', 'Пирамида', 'Цилиндр', 'Конус']
    lis = ttk.Combobox(window, values=r)

    calculate_btn = Button(window, text="Расчитать", command=calculate_cm)
    calculate_btn.place(x=5, y=375)
    draw_btn = Button(window, text="Нарисовать", command=draw_cm)
    draw_btn.place(x=80, y=375)
    clear_btn = Button(window, text="Очистить", command=clear_cm)
    clear_btn.place(x=165, y=375)

    lbl = Label(window)
    lis.place(x=5, y=5)

    blank_drawing()

    lis.bind("<<ComboboxSelected>>", callbackFunc)

    window.mainloop()

