import json
import os
from module1 import calculate_distance  # Імпортуємо функцію

# Ім'я файлу
filename = 'MyData.json'

# Функція для зчитування даних з JSON файлу
def read_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Перевірка наявності необхідних ключів
            if ('coordinates' in data and 'x' in data['coordinates'] and 'y' in data['coordinates'] and 
                'radius' in data and 'language' in data):
                return data
            else:
                print("Некоректні дані в файлі. Введіть нові дані.")
                return None
    else:
        print("Файл не знайдено. Введіть нові дані.")
        return None

# Функція для запису даних у JSON файл
def write_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Дані збережено в файл {filename}")



data = read_data(filename)

if data is not None:
    coordinates = data['coordinates']
    radius = data['radius']
    language = data['language']
    
    # Обчислення відстані до точки A(1, 2)
    point_a = (1, 2)
    point_b = (coordinates['x'], coordinates['y'])
    distance = calculate_distance(point_a, point_b)

    
    
    print(f"Мова: {language}")
    print(f"Відстань до точки A{point_a}: {distance:.3f}")
    print(f"Точка А({coordinates['x'],{coordinates['y']}}) знаходиться всередины окружності радіуса {radius}")
else:
    coords = input("Введіть координати точки A(x, y): ")
    x, y = map(int, coords.split())
    radius = int(input("Введіть радіус окружності R: "))
    language = input("Введіть мову інтерфейсу: ")

    new_data = {
        "coordinates": {
            "x": x,
            "y": y
        },
        "radius": radius,
        "language": language
    }
    write_data(filename, new_data)