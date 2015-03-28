import os

class NMControl:

    base_command = 'nmcli c '
    up_command = 'up '
    down_command = 'down '

    def __init__(self, name):
        self.name = name

    def up(self):
        command = self.base_command + self.up_command + self.name
        res = os.system(command)

        return res

    def down(self):
        command = self.base_command + self.down_command + self.name
        res = os.system(command)

        return res
