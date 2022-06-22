
import enum

class Ability(enum.Enum):
    str = enum.auto()
    dex = enum.auto()
    con = enum.auto()
    int = enum.auto()
    wis = enum.auto()
    cha = enum.auto()


str_ability_map = {
    "str": Ability.str,
    "dex": Ability.dex,
    "con": Ability.con,
    "int": Ability.int,
    "wis": Ability.wis,
    "cha": Ability.cha,
}


def main():
    print("Hello!")


if __name__ == "__main__":
    main()
