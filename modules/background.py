from modules.connections import connection
from abc import ABC, abstractmethod

class Background(ABC):

    def __init__(self, id: int) -> None:
        self.__id = id
        self.__name = ""
        self.__descritpion = ""
        self.__feature = {}

        self.__background()

    def __background(self) -> None:
        with connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT Background.Background, Background.Description, Feature.ID AS FeatureID, Feature.Feature, Feature.Description
                            FROM Background, Feature
                            WHERE Background.ID = ? AND Feature.BackgroundID = Background.ID""", self.__id)

            record = cursor.fetchone()

            self.__name = record.Background
            self.__descritpion = record.Descrition
            self.__feature = {
                "id" : record.FeatureID,
                "feature" : record.Feature,
                "description" : record.Description
            }
    
    @property
    @abstractmethod
    def proficiencies(self) -> list:
        #This will return a list of proficiency ids.
        #This encompases Skills and Tools
        pass

    @property
    @abstractmethod
    def additional_proficiencies(self) -> dict:
        #Some backgrounds allow you to choose from options this will represent this
        #This first kvp will be bool determing if the background has elective proficiencies
        #The second kvp will be the number that can be chosen
        #The third will be the type of proficiency that can be choosen
        #This will include Tools, Skills, and Languages
        pass

    @property
    @abstractmethod
    def equipment(self) -> list:
        #This will return a list of equipment dictionaries 
        pass 

    @property
    @abstractmethod
    def additional_equipment(self) -> dict:
        #Some backgrounds allow you to choose equipment items this will represent this
        #The first kvp will be bool determining if the background has elective equipment
        #The second kvp will be the number that can be chosen
        #The third kvp will be the type of equipment that can be choosen
        pass

    @property
    @abstractmethod
    def gold(self) -> int:
        #Each background adds an amount of gold to the character this will represent that
        pass

    def get_feature(self) -> dict:
        return self.__feature

class Acolyte(Background):

    @property
    def proficiencies(self) -> list:
        proficiencies = [13, 21]
        return proficiencies

    @property
    def additional_proficiencies(self) -> dict:
        proficiencies = {
            "has_elective" : True,
            "electives" : [
                {
                    "number" : 2,
                    "type" : "Language"
                }
            ]
        }
        return proficiencies

    @property
    def equipment(self) -> list:
        #The Inventory Table will need to be filled out first
        pass

    @property
    def additional_equipment(self) -> dict:
        equipment = {
            "has_elective" : False,
            "electives" : []
        }
        return equipment


    @property
    def gold(self) -> int:
        return 15