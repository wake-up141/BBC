import random

ITEMS = ["меч", "аптечка", "монета", "камень"]
#монета и камень это просто хлам

def choose_difficulty():
    print("Выберите сложность:")
    print("1 - Лёгкий")
    print("2 - Нормальный")
    print("3 - Сложный")

    level = None
    while level not in (1, 2, 3):
        s = input("Ваш выбор (1/2/3): ").strip()
        if s.isdigit():
            level = int(s)
        if level not in (1, 2, 3):
            print("Нужно ввести 1, 2 или 3.")

    if level == 1:
        params = {
            "name": "Лёгкий",
            "player_hp": 10,
            "monster_hp": (2, 3),
            "monster_dmg": (1, 1),
            "density": "low",
            "trap_chance": 1,   # из 10
        }
    elif level == 2:
        params = {
            "name": "Нормальный",
            "player_hp": 7,
            "monster_hp": (3, 4),
            "monster_dmg": (1, 2),
            "density": "medium",
            "trap_chance": 2,
        }
    else:
        params = {
            "name": "Сложный",
            "player_hp": 5,
            "monster_hp": (4, 5),
            "monster_dmg": (2, 3),
            "density": "high",
            "trap_chance": 3,
        }

    print("\nВыбрана сложность:", params["name"], "\n")
    return params


def get_lab_size():
    while True:
        try:
            n = int(input("Введите количество строк n: ").strip())
            m = int(input("Введите количество столбцов m: ").strip())
            if n > 0 and m > 0:
                return n, m
            else:
                print("Оба числа должны быть > 0.")
        except ValueError:
            print("Нужно вводить целые числа.")


def generate_labyrinth(n, m, diff):
    density = diff["density"]

    if density == "low":
        base_cells = ["empty"] * 7 + ["chest"] * 2 + ["monster"] * 1
    elif density == "medium":
        base_cells = ["empty"] * 6 + ["chest"] * 2 + ["monster"] * 2
    else:
        base_cells = ["empty"] * 5 + ["chest"] * 1 + ["monster"] * 4

    trap_chance = diff["trap_chance"]

    lab = []
    monsters = []
    chests = []

    hp_min, hp_max = diff["monster_hp"]
    dmg_min, dmg_max = diff["monster_dmg"]

    for y in range(n):
        row_types = []
        row_mon = []
        row_chests = []
        for x in range(m):
            cell_type = random.choice(base_cells)
            if random.randint(1, 10) <= trap_chance:
                cell_type = "trap"

            row_types.append(cell_type)

            if cell_type == "monster":
                hp = random.randint(hp_min, hp_max)
                dmg = random.randint(dmg_min, dmg_max)
                row_mon.append([hp, dmg])
                row_chests.append([])
            elif cell_type == "chest":
                count = random.randint(1, 2)
                items = [random.choice(ITEMS) for _ in range(count)]
                row_chests.append(items)
                row_mon.append(None)
            else:
                row_mon.append(None)
                row_chests.append([])

        lab.append(row_types)
        monsters.append(row_mon)
        chests.append(row_chests)

    empty_cells = []
    for yy in range(n):
        for xx in range(m):
            if lab[yy][xx] == "empty":
                empty_cells.append((xx, yy))

    if not empty_cells:
        ry = random.randrange(n)
        rx = random.randrange(m)
        lab[ry][rx] = "empty"
        monsters[ry][rx] = None
        chests[ry][rx] = []
        empty_cells.append((rx, ry))

    all_cells = [(x, y) for y in range(n) for x in range(m)]

    key_x, key_y = random.choice(all_cells)
    lab[key_y][key_x] = "key"
    monsters[key_y][key_x] = None
    chests[key_y][key_x] = []

    portal_candidates = [(x, y) for (x, y) in all_cells if not (x == key_x and y == key_y)]
    portal_x, portal_y = random.choice(portal_candidates)
    lab[portal_y][portal_x] = "portal"
    monsters[portal_y][portal_x] = None
    chests[portal_y][portal_x] = []

    return lab, monsters, chests


def choose_spawn(lab):
    n = len(lab)
    m = len(lab[0])
    empties = []
    for y in range(n):
        for x in range(m):
            if lab[y][x] == "empty":
                empties.append((x, y))
    return random.choice(empties)


def print_map(lab, visited, player_pos):
    n = len(lab)
    m = len(lab[0])
    px, py = player_pos

    print("\nТекущее поле:")
    for y in range(n):
        row_symbols = []
        for x in range(m):
            if x == px and y == py:
                row_symbols.append("P")
            else:
                if not visited[y][x]:
                    row_symbols.append("o")
                else:
                    t = lab[y][x]
                    if t == "empty":
                        row_symbols.append("x")
                    elif t == "chest":
                        row_symbols.append("c")
                    elif t == "monster":
                        row_symbols.append("m")
                    elif t == "trap":
                        row_symbols.append("t")
                    elif t == "key":
                        row_symbols.append("k")
                    elif t == "portal":
                        row_symbols.append("p")
                    else:
                        row_symbols.append("?")
        print(" ".join(row_symbols))
    print()


def fight(player_hp, base_damage, inventory, mon_stats):
    mon_hp, mon_dmg = mon_stats

    sword_count = inventory.count("меч")
    player_dmg = base_damage + sword_count

    print("\nНачинается бой!")
    print("Ваше HP:", player_hp, "урон:", player_dmg)
    print("Монстр HP:", mon_hp, "урон:", mon_dmg)

    round_num = 1
    while player_hp > 0 and mon_hp > 0:
        print("\nРаунд", round_num)
        mon_hp -= player_dmg
        if mon_hp < 0:
            mon_hp = 0
        print("Вы ударили монстра. HP монстра:", mon_hp)
        if mon_hp <= 0:
            print("Монстр повержен.")
            return player_hp, False

        player_hp -= mon_dmg
        if player_hp < 0:
            player_hp = 0
        print("Монстр ударил вас. Ваше HP:", player_hp)
        if player_hp <= 0:
            print("Вы погибли.")
            return player_hp, True

        round_num += 1

    return player_hp, mon_hp > 0


def use_medkit(player_hp, max_hp):
    heal_value = random.randint(1, 2)
    before = player_hp
    player_hp += heal_value
    if player_hp > max_hp:
        player_hp = max_hp
    healed = player_hp - before
    print("Аптечка восстановила", healed, "HP (", before, "->", player_hp, ")")
    return player_hp


def handle_cell(y, x, lab, monsters, chests, visited,
                player_hp, max_hp, inventory, base_damage):
    visited[y][x] = True
    cell_type = lab[y][x]
    portal_opened = False

    print("\nВы вошли в клетку:", (y, x))

    if cell_type == "empty":
        print("Здесь пусто.")

    elif cell_type == "chest":
        items = chests[y][x]
        if not items:
            print("Пустой сундук.")
        else:
            print("Вы нашли сундук. Внутри:", items)
            for item in items:
                if item == "аптечка":
                    player_hp = use_medkit(player_hp, max_hp)
                else:
                    inventory.append(item)
                    print("Взяли предмет:", item)
            chests[y][x] = []
        lab[y][x] = "empty"
        print("Клетка теперь пустая.")

    elif cell_type == "monster":
        mon = monsters[y][x]
        if mon is None:
            print("Здесь останки монстра.")
            lab[y][x] = "empty"
        else:
            player_hp, mon_alive = fight(player_hp, base_damage, inventory, mon)
            if player_hp <= 0:
                return player_hp, inventory, portal_opened
            if not mon_alive:
                monsters[y][x] = None
                lab[y][x] = "empty"
                print("После боя клетка пустая.")

    elif cell_type == "trap":
        print("Ловушка!")
        player_hp -= 1
        if player_hp < 0:
            player_hp = 0
        print("Ловушка отняла 1 HP. Текущее HP:", player_hp)
        # ловушка остаётся на карте

    elif cell_type == "key":
        if "ключ" in inventory:
            print("Ключ у вас уже есть.")
        else:
            inventory.append("ключ")
            print("Вы нашли ключ!")
        lab[y][x] = "empty"

    elif cell_type == "portal":
        print("Вы нашли портал.")
        if "ключ" in inventory:
            print("Вы используете ключ и открываете портал. Победа!")
            portal_opened = True
        else:
            print("Портал закрыт. Нужен ключ.")


    return player_hp, inventory, portal_opened


def move_player(command, pos, n, m):
    command = command.strip().lower()
    x, y = pos

    if command == "q":
        print("Нельзя выйти, пока не найден ключ и портал.")
        return pos

    dx = 0
    dy = 0
    if command == "w":
        dy = -1
    elif command == "s":
        dy = 1
    elif command == "a":
        dx = -1
    elif command == "d":
        dx = 1
    else:
        print("Команда не распознана. Используйте w/a/s/d или q.")
        return pos

    new_x = x + dx
    new_y = y + dy

    if 0 <= new_x < m and 0 <= new_y < n:
        return (new_x, new_y)
    else:
        print("Нельзя выйти за границы лабиринта.")
        return pos


def main():
    print("Игра: Лабиринт списков")
    n, m = get_lab_size()
    diff = choose_difficulty()

    lab, monsters, chests = generate_labyrinth(n, m, diff)
    spawn_x, spawn_y = choose_spawn(lab)
    player_pos = (spawn_x, spawn_y)

    max_hp = diff["player_hp"]
    player_hp = max_hp
    base_damage = 1
    inventory = []

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[spawn_y][spawn_x] = True

    print("Цель: найти ключ и потом портал.")
    print("Управление: w/a/s/d – ход, q – попытка выхода (до портала не работает).")
    print("Стартовая позиция:", (spawn_y, spawn_x), "\n")

    game_over = False

    while not game_over:
        print_map(lab, visited, player_pos)
        print("HP:", player_hp, "/", max_hp)
        print("Инвентарь:", *inventory)

        cmd = input("Ваш ход (w/a/s/d, q): ")
        new_pos = move_player(cmd, player_pos, n, m)

        if new_pos != player_pos:
            player_pos = new_pos
            x, y = player_pos
            player_hp, inventory, portal_opened = handle_cell(
                y, x, lab, monsters, chests, visited,
                player_hp, max_hp, inventory, base_damage
            )

            if player_hp <= 0:
                print("\nВы погибли. Игра окончена.")
                game_over = True
            elif portal_opened:
                print("\nВы выбрались из лабиринта. Поздравляем!")
                print_map(lab, visited, player_pos)
                game_over = True

    print("Спасибо за игру.")

main()
