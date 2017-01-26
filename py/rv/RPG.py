# A design test for dynamic class building.
#     > attributes and conditional logic are readed from a dictionary.

# This dictionary will actually reside in another file, maybe a json or
# gzipped pickled json...
WEAPONS = {
    "bastard's sting": {
        "equipped": False,
        "magic": 2,
        "on_turn_actions": [],
        "on_hit_actions": [],
        "on_equip": [
            {
                "type": "check",
                "condition": (
                    "self.owner.is_of_class",
                    ["antipaladin"]
                ),
                True: [
                    {
                        "type": "action",
                        "action": "self.add_on_hit",
                        "args": ["unholy"]
                    },
                    {
                        "type": "action",
                        "action": "self.add_on_turn",
                        "args": ["unholy aurea"]
                    },
                    {
                        "type": "action",
                        "action": "self.set_attribute",
                        "args": ["magic", 5]
                    }
                ],
                False: [
                    {
                        "type": "action",
                        "action": "self.set_attribute",
                        "args": ["magic", 2]
                    }
                ]
            }
        ],
        "on_unequip": [
            {
                "type": "action",
                "action": "self.rem_on_hit",
                "args": ["unholy"]
            },
            {
                "type": "action",
                "action": "self.rem_on_turn",
                "args": ["unholy_aurea"]
            },
            {
                "type": "action",
                "action": "self.set_attribute",
                "args": ["self.magic", 2]
            }
        ]
    }
}


class Player:

    inventory = []

    def __init__(self, _class):
        self._class = _class

    def pick_up(self, item):
        """Pick an object, put in inventory, set its owner."""
        self.inventory.append(item)
        item.owner = self

    def is_of_class(self, _class):
        return self._class == _class


class Weapon:
    """An type of item that can be equipped/used to attack."""

    def __init__(self, template):
        """Set the parameters based on a template."""
        self.__dict__.update(WEAPONS[template])

    def equip(self):
        """Set item status and call its on equip functions."""
        self.equipped = True
        for action in self.on_equip:
            if action['type'] == "check":
                self.check(action)
            elif action['type'] == "action":
                self.action(action)

    def unequip(self):
        """Unset item dynamic status, call its on unequip functions."""
        self.equipped = False
        for action in self.on_unequip:
            if action['type'] == "check":
                self.check(action)
            elif action['type'] == "action":
                self.action(action)

    def check(self, dic):
        """Check a condition and call an action according to it."""
        check_act = eval(dic['condition'][0])
        args = dic['condition'][1]
        result = check_act(*args)

        self.action(*dic[result])

    def action(self, *dicts):
        """Perform action with args, both specified on dicts."""
        for dic in dicts:
            act = eval(dic['action'])
            act(dic['args'])

    def set_attribute(self, args):
        name, value = args
        setattr(self, name, value)

    def add_on_hit(self, actions):
        for action in actions:
            if action not in self.on_hit_actions:
                self.on_hit_actions.append(action)

    def add_on_turn(self, actions):
        for action in actions:
            if action not in self.on_turn_actions:
                self.on_turn_actions.append(action)

    def rem_on_hit(self, actions):
        for action in actions:
            try:
                self.on_hit_actions.remove(action)
            except ValueError:
                # We never had that but unequip tries to clean it anyway.
                pass

    def rem_on_turn(self, actions):
        for action in actions:
            try:
                self.on_turn_actions.remove(action)
            except ValueError:
                pass

if __name__ == '__main__':
    """Let's test it!"""

    weapon = Weapon("bastard's sting")
    player1 = Player("paladin")
    player1.pick_up(weapon)
    weapon.equip()
    print("Enhancement: {}, Hit effects: {}, Other effects: {}".format(
        weapon.magic, weapon.on_hit_actions, weapon.on_turn_actions))
    weapon.unequip()

    player2 = Player("antipaladin")
    player2.pick_up(weapon)
    weapon.equip()
    print("Enhancement: {}, Hit effects: {}, Other effects: {}".format(
        weapon.magic, weapon.on_hit_actions, weapon.on_turn_actions))
