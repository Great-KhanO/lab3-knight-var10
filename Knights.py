from collections import deque
from typing import Tuple

BOARD_MIN = 1
BOARD_MAX = 8

KNIGHT_MOVES = (
  (-2, -1), (-2, 1),
  (-1, -2), (-1, 2),
  (1, -2),  (1, 2),
  (2, -1),  (2, 1),
)


def _validate_position(pos: Tuple[int, int], name: str) -> None:
  """Проверяет, что позиция — кортеж из двух целых чисел в диапазоне [1, 8]."""
  if not isinstance(pos, tuple) or len(pos) != 2:
    raise ValueError(f"{name} должен быть кортежем из двух целых чисел.")
  x, y = pos
  if isinstance(x, bool) or isinstance(y, bool) or not (isinstance(x, int) and isinstance(y, int)):
    raise ValueError(f"Координаты {name} должны быть целыми числами.")
  if not (BOARD_MIN <= x <= BOARD_MAX and BOARD_MIN <= y <= BOARD_MAX):
    raise ValueError(f"Координаты {name} должны быть в диапазоне от 1 до 8, получено {pos}.")


def knight_move(start: Tuple[int, int], finish: Tuple[int, int]) -> int:
  """Вычисляет минимальное количество ходов коня из клетки start в finish."""
  _validate_position(start, "start")
  _validate_position(finish, "finish")

  if start == finish:
    return 0

  visited = {start}
  queue = deque([(start[0], start[1], 0)])

  while queue:
    x, y, moves = queue.popleft()
    for dx, dy in KNIGHT_MOVES:
      nx, ny = x + dx, y + dy
      if BOARD_MIN <= nx <= BOARD_MAX and BOARD_MIN <= ny <= BOARD_MAX:
        if (nx, ny) == finish:
          return moves + 1
        if (nx, ny) not in visited:
          visited.add((nx, ny))
          queue.append((nx, ny, moves + 1))

  return -1

def knights_collision(first: Tuple[int, int], second: Tuple[int, int]) -> int:
  """
  Вычисляет минимальное количество одновременных ходов, через которое
  встретятся два коня, находящиеся на клетках first и second.
  Если клетки разного цвета, встреча невозможна — возвращается -1.
  """
  _validate_position(first, "first")
  _validate_position(second, "second")

  if first == second:
    return 0

  # Каждый ход меняет цвет клетки (чётность x + y).
  # При разной чётности стартовых клеток одновременная встреча невозможна.
  if (first[0] + first[1]) % 2 != (second[0] + second[1]) % 2:
    return -1

  return knight_move(first, second) // 2