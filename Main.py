from Knights import knight_move, knights_collision


def run_demo() -> None:
  print("=== Демонстрация функции knight_move(start, finish) ===")
  move_tests = [
    ((5, 5), (7, 6)),  # 1 ход «буквой Г» (e5 -> g6)
    ((1, 1), (1, 1)),  # стартовая и конечная клетки совпадают
    ((1, 1), (1, 2)),  # соседняя клетка у края доски
    ((1, 1), (2, 2)),  # диагонально соседняя клетка из угла
    ((4, 4), (5, 5)),  # диагонально соседняя клетка в центре
    ((1, 1), (3, 3)),  # диагональ через одну клетку
    ((1, 1), (8, 8)),  # противоположные углы доски (a1 -> h8)
  ]

  for start, finish in move_tests:
    result = knight_move(start, finish)
    print(f"knight_move({start}, {finish}) -> {result}")

  print("\n=== Демонстрация функции knights_collision(first, second) ===")
  collision_tests = [
    ((4, 4), (5, 5)),  # 1 ход
    ((1, 1), (3, 3)),  # 2 хода
    ((1, 1), (8, 8)),  # 3 хода
    ((1, 1), (1, 1)),  # 0 ходов (уже на одной клетке)
    ((1, 1), (1, 2)),  # клетки разного цвета -> встреча невозможна (-1)
    ((1, 1), (2, 3)),  # клетки разного цвета -> встреча невозможна (-1)
  ]

  for first, second in collision_tests:
    result = knights_collision(first, second)
    status = f"{result} ход(а/ов)" if result != -1 else "-1 (встреча невозможна)"
    print(f"knights_collision({first}, {second}) -> {status}")

  print("\n=== Проверка обработки некорректных координат ===")
  try:
    knight_move((0, 5), (4, 4))
  except ValueError as err:
    print(f"knight_move((0, 5), (4, 4)) -> ValueError: {err}")


if __name__ == "__main__":
  run_demo()