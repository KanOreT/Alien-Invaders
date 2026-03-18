import os

# Налаштування поля
WIDTH = 30
HEIGHT = 15

# Початкові координати гравця (внизу по центру)
player_x = WIDTH // 2
player_y = HEIGHT - 1

# Список для зберігання снарядів (кожен снаряд - це список [x, y])
bullets = []

def draw_field():
    # Очищуємо консоль
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Керування: 'a' - вліво, 'd' - вправо, 'w' - постріл, Enter - пропуск")
    print("-" * (WIDTH + 2)) # Верхня межа

    for y in range(HEIGHT):
        line = "|" # Ліва межа
        for x in range(WIDTH):
            # Перевіряємо, чи є тут гравець
            if x == player_x and y == player_y:
                line += "A"
            # Перевіряємо, чи є тут снаряд
            else:
                is_bullet = False
                for b in bullets:
                    if b[0] == x and b[1] == y:
                        is_bullet = True
                        break
                
                if is_bullet:
                    line += "|"
                else:
                    line += " " # Порожнє місце
        
        line += "|" # Права межа
        print(line)

    print("-" * (WIDTH + 2)) # Нижня межа

# Головний ігровий цикл
while True:
    draw_field()
    
    # Отримуємо ввід від користувача
    command = input("Ваш хід: ").lower()

    # 1. Логіка руху гравця
    if command == 'a' and player_x > 0:
        player_x -= 1
    elif command == 'd' and player_x < WIDTH - 1:
        player_x += 1
    elif command == 'w':
        # Створюємо новий снаряд прямо над гравцем
        bullets.append([player_x, player_y - 1])

    # 2. Логіка руху снарядів (вони летять вгору на кожному кроці)
    for b in bullets:
        b[1] -= 1 # Зменшуємо y, щоб снаряд летів вгору

    # 3. Видаляємо снаряди, які вилетіли за межі поля
    # (Створюємо новий список тільки з тими, що всередині поля)
    bullets = [b for b in bullets if b[1] >= 0]

    # Вихід з гри (просто для зручності)
    if command == 'exit':
        break
