Nice code! Clean, and pretty Pythonic IMO. Without further ado...

# General stuff

```
# This dictionary will actually reside in another file, maybe a json or
# gzipped pickled json...
WEAPONS = {
}
```
The first time I read this post, I was like "this guy is out of his mind" for the ridiculous nesting abuse of the dictionary syntax. Now I understand :)

```
item.owner = self
```
This is interesting to me. `item` is already privately initialised for a given instance; why the redundancy?
It reads well, but I don't understand why it makes sense.

```
def is_of_class(self, _class):
  return self._class == _class
```
Nitpick: Python already has two ways to check if something is a subclass / instance of something.
I think the name of this method should be `is_instanceof` or so -- I know I'd be more likely to remember that, anyways.

# Code duplication
Let's take a look at this:

```
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

# --------------

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

# --------------
<snip></snip>

def add_on_hit(self, actions):
    for action in actions:
        if action not in self.on_hit_actions:
            self.on_hit_actions.append(action)

def add_on_turn(self, actions):
    for action in actions:
        if action not in self.on_turn_actions:
            self.on_turn_actions.append(action)

# --------------

def rem_on_hit(self, actions):
    for action in actions:
        try:
            self.on_hit_actions.remove(action)
        except ValueError:
            pass

def rem_on_turn(self, actions):
    for action in actions:
        try:
            self.on_turn_actions.remove(action)
        except ValueError:
            pass
```
Notice anything... macro? To me, what stands out is that each of the methods in the groups shares a literally identical *shape* to the eye when glancing over it, and upon closer inspection they each do the *exact* same thing in some different semantic context.

Whenever I come across cases of this all-but-semantic-duplication in my own code, my solution (typically) is to write *one* method that takes arguments of `do.what`, `to.what`, `how`, etc. Generally, I think code that actually does something good and minimises duplication, even if that one method does get lengthy, is overall better than duplicated methods.

I could go into my spiel about why I think code deduplication is important, but you've probably heard it before and if you haven't, you can just google "why code duplication is evil" or so.

---

Other than that stuff, I would just add writing to some log when the `ValueError` catches, rather than just pass -- even if you want to ignore it now, you may want to refactor your code for speed in the future: EAFP is not necessarily faster or more efficient than LBYL, and if that time comes you will appreciate having logs about the behvaiour. Aside from logging, there could be an unexpected reason that throws `ValueError`, the cause of bugs, and logs never hurt debugging.