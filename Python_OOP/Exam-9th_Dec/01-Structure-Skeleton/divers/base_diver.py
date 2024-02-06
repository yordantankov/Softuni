from project.fish.base_fish import BaseFish
from abc import ABC,abstractmethod
from typing import List


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List[BaseFish] = []
        self.competition_points = 0.0
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value:str):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value
    @property
    def oxygen_level(self):
        return self.__oxygen_level
    @oxygen_level.setter
    def oxygen_level(self, value:int):
        if value<0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value
    @abstractmethod
    def miss(self, time_to_catch: int):
        pass
    @abstractmethod
    def renew_oxy(self):
        pass
    def hit(self, fish: BaseFish):
        result = self.oxygen_level - fish.time_to_catch
        if result < 0:
            self.has_health_issue = True
            self.oxygen_level = 0
        if result >= 0:
            self.oxygen_level = result
            self.catch.append(fish)
            self.competition_points += fish.points
    def update_health_status(self):
        if self.has_health_issue:
            self.has_health_issue = False
        if not self.has_health_issue:
            self.has_health_issue = True
    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}," \
               f" Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"