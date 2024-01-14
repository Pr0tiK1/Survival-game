RESET = "\033[0m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RED = "\033[31m"
WHITE = "\033[97m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

class Tile:
    def __init__(self, symbol: str, color: str | None = None):
        self.symbol = f"{color}{symbol}{RESET}" if color else symbol


plains = Tile("-", GREEN)
forest = Tile("T", GREEN)
pines = Tile(":", YELLOW)
mountain = Tile("A", WHITE)
water = Tile("~", CYAN)