from tkinter import *
from tkinter import ttk
import FlatFigures as FlatFigures
import VolumetricFigures as VolumetricFigures

window = Tk()
vidgets = []
params = []
vert_gl = 0

def clicked():
    if lis.get() == 'Круг':
         p = int(params[0].get())
         circle_obj = FlatFigures.Сircle(p)
         area = circle_obj.areaСircle()
         diametr = circle_obj.diametr()
         mass_rez =[area,diametr]
         output_result(mass_rez,len(params)*20+30)
         circle_obj.printCircle()
    elif lis.get() == 'Квадрат':
         p = int(params[0].get())
         square_obj = FlatFigures.Square(p)
         area = square_obj.areaSquare()
         perimeter = square_obj.perimetrSquare2()
         mass_rez = [area,perimeter]
         output_result(mass_rez, len(params) * 20 + 30)
         square_obj.PrintSquare()
    elif lis.get() == 'Прямоугольник':
         x = int(params[0].get())
         y = int(params[1].get())
         rectangle_obj = FlatFigures.Rectangle(x,y)
         area = rectangle_obj.areaRectangle()
         perimeter = rectangle_obj.perimetr()
         mass_rez = [area, perimeter]
         output_result(mass_rez, len(params) * 20 + 30)
         rectangle_obj.PrintRectangle()
    elif lis.get() == 'Треугольник':
         triangle_obj = FlatFigures.Triangle(int(params[0].get()),int(params[1].get()),int(params[2].get()))
         area = triangle_obj.areaTriangle()
         perimeter = triangle_obj.perimetr()
         mass_rez = [area, perimeter]
         output_result(mass_rez, len(params) * 20 + 30)
         triangle_obj.PrintTriangle()
    elif lis.get() == 'Трапеция':
         Trapeze_obj = FlatFigures.Trapeze(int(params[0].get()),int(params[1].get()),int(params[2].get()),
                                        int(params[3].get()),int(params[4].get()))
         area = Trapeze_obj.areaTrapeze()
         perimeter = Trapeze_obj.perimetr()
         mass_rez = [area, perimeter]
         output_result(mass_rez, len(params) * 20 + 30)
         Trapeze_obj.PrintTrapeze()
    elif lis.get() == 'Ромб':
         Rhombus_obj = FlatFigures.Rhombus(int(params[0].get()))
         area = Rhombus_obj.area_Rhombus()
         perimeter = Rhombus_obj.perimetr_Rhombus()
         mass_rez = [area, perimeter]
         output_result(mass_rez, len(params) * 20 + 30)
         Rhombus_obj.PrintRhombus()
    elif lis.get() == 'Сфера':
         p = int(params[0].get())
         sphere_obj = VolumetricFigures.sphere(p)
         area = sphere_obj.areasphere()
         diametr = sphere_obj.obem()
         mass_rez = [area, diametr]
         output_result(mass_rez, len(params) * 20 + 30)
         sphere_obj.PrintSphere()
    elif lis.get() == 'Куб':
         p = int(params[0].get())
         cube_obj = VolumetricFigures.cube(p)
         area = cube_obj.areacube()
         volume = cube_obj.volume()
         mass_rez = [area, volume]
         output_result(mass_rez, len(params) * 20 + 30)
         cube_obj.PrintСube()
    elif lis.get() == 'Параллелепипед':
         parallelepiped_obj = VolumetricFigures.parallelepiped(int(params[0].get()), int(params[1].get()), int(params[2].get()))
         area = parallelepiped_obj.areaparallelepiped()
         volume = parallelepiped_obj.volume()
         mass_rez = [area, volume]
         output_result(mass_rez, len(params) * 20 + 30)
         parallelepiped_obj.Printparallelepiped()
    elif lis.get() == 'Пирамида':
         Pyramid_obj = VolumetricFigures.Pyramid(int(params[0].get()), int(params[1].get()), int(params[2].get()))
         area = Pyramid_obj.areaPyramid()
         volume = Pyramid_obj.volume()
         mass_rez = [area, volume]
         output_result(mass_rez, len(params) * 20 + 30)
         Pyramid_obj.PrintPyramid()
    elif lis.get() == 'Цилиндр':
         cylinder_obj = VolumetricFigures.cylinder(int(params[0].get()), int(params[1].get()))
         area = cylinder_obj.areacylinder()
         volume = cylinder_obj.volume()
         mass_rez = [area, volume]
         output_result(mass_rez, len(params) * 20 + 30)
         cylinder_obj.Printparallelepiped()
    elif lis.get() == 'Конус':
         cone_obj = VolumetricFigures.cone(int(params[0].get()), int(params[1].get()))
         area = cone_obj.areacone()
         volume = cone_obj.volume()
         mass_rez = [area, volume]
         output_result(mass_rez, len(params) * 20 + 30)
         cone_obj.Printcone()

def output_result(mass_rez,vert):
    vert + 30
    for i in mass_rez:
        lbl = Label(window, text=i)
        lbl.place(x=0, y=vert)
        vert = vert+30
        vidgets.append(lbl)

def clicked2():
    blank_drawing()
    our_image = PhotoImage(file="saved_figure-tight.png")
    width_our_image = our_image.width()
    if width_our_image > 500:
        our_image = our_image.subsample(2, 2)
    our_label = Label(window)
    our_label.image = our_image
    our_label['image'] = our_label.image
    our_label.place(x=390, y=0)

def clicked3():
    blank_drawing()
    for i in vidgets:
        i.destroy()
    for i in params:
        i.destroy()

def obrabotkaSob(nameobg):
    clicked3()
    if nameobg == 'Круг':
        parameter_list = FlatFigures.Сircle.output_parameters()
        fill_parameters(parameter_list, 160)
    elif nameobg == 'Квадрат':
        parameter_list = FlatFigures.Square.output_parameters()
        fill_parameters(parameter_list, 230)
    elif nameobg == 'Прямоугольник':
        parameter_list = FlatFigures.Rectangle.output_parameters()
        fill_parameters(parameter_list, 260)
    elif nameobg == 'Треугольник':
        parameter_list = FlatFigures.Triangle.output_parameters()
        fill_parameters(parameter_list,325)
    elif nameobg == 'Сфера':
        parameter_list = VolumetricFigures.sphere.output_parameters()
        fill_parameters(parameter_list,325)
    elif nameobg == 'Куб':
        parameter_list = VolumetricFigures.cube.output_parameters()
        fill_parameters(parameter_list, 325)
    elif nameobg == 'Параллелепипед':
        parameter_list = VolumetricFigures.parallelepiped.output_parameters()
        fill_parameters(parameter_list, 325)
    elif nameobg == 'Пирамида':
        parameter_list = VolumetricFigures.Pyramid.output_parameters()
        fill_parameters(parameter_list, 325)
    elif nameobg == 'Цилиндр':
        parameter_list = VolumetricFigures.cylinder.output_parameters()
        fill_parameters(parameter_list, 325)
    elif nameobg == 'Конус':
        parameter_list = VolumetricFigures.cone.output_parameters()
        fill_parameters(parameter_list, 325)
    elif nameobg == 'Трапеция':
        parameter_list  = FlatFigures.Trapeze.output_parameters()
        fill_parameters(parameter_list, 325)
    elif nameobg == 'Ромб':
        parameter_list = FlatFigures.Rhombus.output_parameters()
        fill_parameters(parameter_list, 325)

def fill_parameters (SpicokParam,gor):
    vert = 30
    params.clear()
    for x in SpicokParam:
        lbl = Label(window, text=x)
        lbl.place(x=0, y=vert)
        param = Entry(window, width=10)
        param.place(x=gor, y=vert)
        vidgets.append(lbl)
        params.append(param)
        vert = vert + 20

def callbackFunc(event):
    obrabotkaSob(lis.get())

def blank_drawing ():
    our_image = PhotoImage(file="saved_figure-tigh1t.png")
    our_image = our_image.subsample(1, 1)
    our_label = Label(window)
    our_label.image = our_image
    our_label['image'] = our_label.image
    our_label.place(x=390, y=0)

if __name__ == '__main__':
    window.title("Геометрический калькулятор")
    window.geometry('800x410')
    selected = IntVar()

    r = ['Круг', 'Квадрат', 'Прямоугольник', 'Треугольник', 'Трапеция', 'Ромб', 'Сфера'
        , 'Куб', 'Параллелепипед', 'Пирамида', 'Цилиндр', 'Конус']
    lis = ttk.Combobox(window, values=r)

    btn = Button(window, text="Расчитать", command=clicked)
    btn2 = Button(window, text="Нарисовать", command=clicked2)
    btn3 = Button(window, text="Очистить", command=clicked3)

    lbl = Label(window)
    lis.place(x=5, y=5)
    btn.place(x=5, y=375)
    btn2.place(x=80, y=375)
    btn3.place(x=165, y=375)
    blank_drawing()

    lis.bind("<<ComboboxSelected>>", callbackFunc)

    window.mainloop()

