from modules.connections import connection
from abc import ABC, abstractmethod

class Race(ABC):

    def __init__(self, id: int) -> None:
        self.__id = id
        self.__name = ""

        self.__race()

    def __race(self) -> None:
        with connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT Race
                            FROM Race
                            WHERE ID = ?""")

            record = cursor.fetchone()

            self.__name = record.Race

class Dwarf(Race):
    pass

class Elf(Race):
    pass

class Halfling(Race):
    pass

class Human(Race):
    pass

class Dragonborn(Race):
    pass

class Gnome(Race):
    pass

class Half_Elf(Race):
    pass

class Half_Orc(Race):
    pass

class Tiefling(Race):
    pass

class Aasimar(Race):
    pass

class Firbolg(Race):
    pass

class Goliath(Race):
    pass

class Kenku(Race):
    pass

class LizardFolk(Race):
    pass

class Tabaxi(Race):
    pass

class Trition(Race):
    pass

class Bugbear(Race):
    pass

class Goblin(Race):
    pass

class Hobgoblin(Race):
    pass

class Kobold(Race):
    pass

class Orc(Race):
    pass

class Yuan_Ti_Pureblood(Race):
    pass

class Gith(Race): 
    pass