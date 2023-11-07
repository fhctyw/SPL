class MenuItem:
    def __init__(self, name: str, action=None):
        self.name = name
        self.action = action
        self.sub_menu = {}

    def add(self, name: str, action=None):
        self.sub_menu[name] = MenuItem(name, action)
        return self.sub_menu[name]

    def __getitem__(self, key: str):
        return self.sub_menu.get(key, None)

    def execute(self):
        if self.action:
            self.action()