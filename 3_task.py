print('Напишите программу, которая принимает на вход координаты точки (X и Y), '
      '\nпричём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, '
      '\nв которой находится эта точка (или на какой оси она находится).')
variable_x = int(input("Введите координату Х --> "))
variable_y = int(input("Введите координату Y --> "))
if variable_x != 0 and variable_y != 0:
      if variable_x > 0 and variable_y > 0:
            print("Это (I) первая четверть")
      elif variable_x < 0 and variable_y > 0:
            print("Это (II) вторая четверть")
      elif variable_x < 0 and variable_y < 0:
            print("Это (III) третья четверть")
      else:
            print("Это (IV) четвертая четверть")
else:
      print("Вы ввели недопустимые значения. Перепроверьте правильность ввода данных")