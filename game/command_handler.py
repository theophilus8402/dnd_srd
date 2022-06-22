

class Command():

    def __init__(self):
        pass

    def execute(self):
        pass


class CommandHandler():

    def __init__(self, entity):
        self.entity = entity
        self.commands = []
        self.cmd_index = 0
        self.undone_cmds = []

    def undo(self):
        cmd = self.commands.pop()
        cmd.undo()
        self.undone_cmds.append(cmd)

    def redo(self):
        cmd = self.undone_cmds.pop()
        cmd.execute()
        self.commands.append(cmd)


def main():
    print("Hello!")


if __name__ == "__main__":
    main()
