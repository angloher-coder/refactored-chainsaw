class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def interact(self):
        raise NotImplementedError("Subclasses must implement 'interact()' method.")

class Player(Character):
    def __init__(self, name, description):
        super().__init__(name, description)

    def interact(self):
        print("You are interacting with yourself.")

class NPC(Character):
    def __init__(self, name, description, dialog):
        super().__init__(name, description)
        self.dialog = dialog

    def interact(self):
        print(f"{self.name}: {self.dialog}")

# Add more classes for Location, Items, etc.

def main():
    player = Player("You", "A brave adventurer.")
    npc = NPC("Old Man", "An old man with a long beard.", "Welcome to the adventure!")

    print(player.description)
    npc.interact()

if __name__ == "__main__":
    main()
