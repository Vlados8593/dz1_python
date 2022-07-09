print('Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z '
      '\nдля всех значений предикат.')
def logic(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return bool( (not (x or y or z)) == (not x and not y and not z) )

if (logic(0, 0, 0) and logic(0, 0, 1) and logic(0, 1, 0) and logic(0, 1, 1) and logic(1, 0, 0)
        and logic(1, 0, 1) and logic(1, 1, 0) and logic(1, 1, 1)) == 1:
    print('True')
else:
    print('Not true. LoL')