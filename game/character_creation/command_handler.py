
from command_handler import Command, CommandHandler
from character_creation.ability_scores import str_ability_map

class SetAbilityCommand(Command):

    def __init__(self, entity, ability, score):
        self.entity = entity
        self.ability = ability
        self.score = score

    def execute(self):
        print("run!")
        self.orig_ability_score = self.entity.ability_scores[self.ability]
        self.entity.ability_scores[self.ability] = self.score

    def undo(self):
        print("undo!")
        self.entity.ability_scores[self.ability] = self.orig_ability_score

    def __repr__(self):
        return f"<ab {self.ability} {self.score}>"


class CharacterCreatorCommandHandler(CommandHandler):

    def __init__(self, entity):
        super().__init__(entity)

    def handle_input(self, command):
        match command.split():
            case ["set", ab, value]:
                if not ab in str_ability_map.keys():
                    str_abs = ", ".join(list(str_ability_map.keys()))
                    print(f"Need to choose one of the following: {str_abs}")
                    return
                try:
                    int_value = int(value)
                except ValueError:
                    print("Need to choose an ability score between 1 and 18.")
                    return
                ability = str_ability_map[ab]
                print(f"set {ability} {value}")
                new_ab_cmd = SetAbilityCommand(self.entity, ability, int_value)
                new_ab_cmd.execute()
                self.commands.append(new_ab_cmd)

            case ["u"]:
                print("Undo!")
                self.undo()

            case ["r"]:
                print("Redo!")
                self.redo()


def main():
    print("Hello!")


if __name__ == "__main__":
    main()
