"""A module with classes for a walking game"""


class Room():
    defeated = []
    """Room class"""
    def __init__(self, place):
        """
        Initializes a class
        """
        self.place = place
        self.item = None
        self.character = None

    def set_description(self, message):
        """
        Sets a description for a room
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        >>> kitchen.description
        'A dank and dirty room buzzing with flies.'
        """
        self.description = message

    def __str__(self):
        """Returns a str - name of a room"""
        return f"{self.place}"
    
    def link_room(self, some_place, part):
        """
        Links a room to its neighbour
        >>> kitchen = Room("Kitchen")
        >>> hall = Room("Hall")
        >>> kitchen.link_room(hall, "west")
        >>> kitchen.linked.keys()
        ['west']
        """
        if "linked" in dir(self):
            self.linked[part] = some_place
        else:
            self.linked = dict()
            self.linked[part] = some_place

    def move(self, command):
        """
        Returns another room by its place in linked rooms
        """
        return self.linked[command]

    def get_details(self):
        """
        Prints room details
        """
        print(self.place)
        print("-"*20)
        print(self.description)
        if "linked" in dir(self):
            for part, room in self.linked.items():
                print("The", room, "is", part)

    def get_item(self):
        """
        Returns an item in the room
        """
        return self.item

    def get_character(self):
        """
        Returns a character in the room
        """
        return self.character

    def set_item(self, item):
        """
        Sets an item into the room
        """
        self.item = item

    def set_character(self, character):
        """
        Sets a character into the room
        """
        self.character = character
        character.roomin = self

class Character():
    """Basic class for living creatures"""
    def __init__(self, name, description):
        """
        Initializes a class
        """
        self.name = name
        self.description = description

    def describe(self):
        """
        Prints info about this object.
        """
        print(self.name, "is here!")
        print(self.description)

class Enemy(Character):
    """Enemy for a protaginist, can fight and talk"""
    def __init__(self, name, description):
        """
        Initializes a class
        """
        super().__init__(name, description)
        self.roomin = None

    def set_conversation(self, message):
        """Sets a response for talking"""
        self.response = message

    def set_weakness(self, weakness):
        """Sets a weakness of this enemy"""
        self.weakness = weakness

    def talk(self):
        """
        Prints enemy's response
        """
        print(f"[{self.name} says]: {self.response}")

    def fight(self, item):
        """Determines a victory or loss"""
        if self.weakness == item:
            self.roomin.defeated.append(1)
            print(f"You fend {self.name} off with the {item}")
            return True
        print(f"{self.name} crushes you, puny adventurer!")
        return False

    def get_defeated(self):
        """
        Checks how many enemies are gone
        """
        return len(self.roomin.defeated)

class Friend(Character):
    """Class for friendly creatures"""
    def __init__(self, name, description):
        """
        Initializes a class
        """
        super().__init__(name, description)

class Item():
    """Item class"""
    def __init__(self, name):
        """
        Initializes a class
        """
        self.name = name

    def set_description(self, message):
        """
        Sets a description to the item.
        """
        self.description = message

    def describe(self):
        """
        Prints info about the item
        """
        print(f"The [{self.name}] is here -", self.description)

    def get_name(self):
        """
        Returns a name of an item
        """
        return self.name





# kitchen = Room("Kitchen")
# kitchen.set_description("A dank and dirty room buzzing with flies.")
# hall = Room("Hall")
# hall.set_description("Just fire in a hall")

# kitchen.link_room(hall, "west")
# kitchen.get_details()
# hall.get_details()
