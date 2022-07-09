print("Напишите программу, которая принимает на вход координаты двух точек и "
      "\nнаходит расстояние между ними в 2D пространстве.")
variable_x1 = int(input("Введите координаты точки A, x --> "))
variable_y1 = int(input("Введите координаты точки A, y --> "))
variable_x2 = int(input("Введите координаты точки B, x --> "))
variable_y2 = int(input("Введите координаты точки B, y --> "))

def find_coordinates(x1,y1,x2,y2):
    result = (( (x2-x1)**2 ) + ( (y2-y1)**2 ))**0.5
    print(f"Расстояние между точками - {result}")

find_coordinates(variable_x1, variable_y1, variable_x2, variable_y2)