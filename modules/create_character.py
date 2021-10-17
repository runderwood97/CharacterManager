from modules.connections import connection
from modules.race import *
from modules.sub_race import *
from modules.main_class import *
from modules.sub_class import *
from modules.background import *

class Create_Character:

    def __init__(self, race_id: int, sub_race_id: int, main_class_id: int, sub_class_id: int, background_id: int, name: str, level: int,
                    alignment: str, strength: int, dexterity: int, constitution: int, intelligence: int, wisdom: int, charisma: int, hit_points: int,
                    speed: int, copper: int, silver: int, gold: int, platnum: int, user_id: int) -> None:

        self.__name = name
        self.__level = level
        self.__alignment = alignment
        self.__strength = strength
        self.__dexterity = dexterity
        self.__constitution = constitution
        self.__intelligence = intelligence
        self.__wisdom = wisdom
        self.__charisma = charisma
        self.__hit_points = hit_points
        self.__speed = speed
        self.__copper = copper
        self.__silver = silver
        self.__gold = gold
        self.__platnum = platnum
        self.__user_id = user_id

        self.__race =  self.__set_race(race_id)
        self.__sub_race = self.__set_sub_race(sub_race_id)
        self.__main_class = self.__set_main_class(main_class_id)
        self.__sub_class = self.__set_sub_class(sub_class_id)
        self.__background = self.__set_background(background_id)

        self.__id = self.__create_character()

    def __set_race(self, race_id: int) -> Race:
        pass

    def __set_sub_race(self, sub_race_id: int) -> Sub_Race:
        pass

    def __set_main_class(self, main_class_id: int) -> Main_Class:
        pass

    def __set_sub_class(self, sub_class_id: int) -> Sub_Class:
        pass

    def __set_background(self, background_id: int) -> Background:
        pass

    def __create_character(self) -> int:
        pass

    def add_proficiencies(self, additional_proficiencies: list) -> None:
        #This will need to grab all the proficiencies from the class, subclass, race, subrace, and backgrounds along with the electives
        pass