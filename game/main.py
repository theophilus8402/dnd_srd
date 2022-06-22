
import enum

from character_creation.ability_scores import Ability, str_ability_map
from character_creation.command_handler import SetAbilityCommand, CharacterCreatorCommandHandler


class Entity():

    def __init__(self, name):
        self.name = name
        self.ability_scores = {
            Ability.str : 0,
            Ability.dex : 0,
            Ability.con : 0,
            Ability.int : 0,
            Ability.wis : 0,
            Ability.cha : 0,
        }

    def __repr__(self):
        return f"<{self.name} str:{self.ability_scores[Ability.str]}>"


def get_command_handler(entity):
    return entity.command_handler


def main():

    entity = Entity("bob")
    entity.command_handler = CharacterCreatorCommandHandler(entity)

    while True:

        command = input("set a stat (i.e. 'set str 12'): ").lower()
        command_handler = get_command_handler(entity)
        command_handler.handle_input(command)
        print(f"Cmds: {command_handler.commands}")
        print(entity)


if __name__ == "__main__":
    main()
