from project.divers.base_diver import BaseDiver
import math


class FreeDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 120)
        self.capacity = 120

    def miss(self, time_to_catch: int):
        self.oxygen_level -= 0.6 * time_to_catch
        if self.oxygen_level < 0 or self.oxygen_level == 0:
            self.has_health_issue = True
            self.oxygen_level = 0
        self.oxygen_level = round(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = 120
