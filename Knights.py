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