from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish
from typing import List

class NauticalCatchChallengeApp:
    ALLOWED_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    ALLOWED_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []
    def dive_into_competition(self,diver_type: str, diver_name: str):
        if diver_type not in self.ALLOWED_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        for d in self.divers:
            if d.name == diver_name:
                return f"{diver_name} is already a participant."
        diver = self.ALLOWED_DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self,fish_type: str, fish_name: str, points: float):
        if fish_type not in self.ALLOWED_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."
        for f in self.fish_list:
            if f.name == fish_name:
                return f"{fish_name} is already permitted."
        fish = self.ALLOWED_FISH[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self,diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver.name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.oxygen_level = 0
            diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky is True:
                diver.hit(fish)
                self.ox_lvl(diver)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."#possible error
            if is_lucky is False:
                diver.miss(fish.time_to_catch)
                self.ox_lvl(diver)
                return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            self.ox_lvl(diver)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        br = 0
        for d in self.divers:
            if d.has_health_issue or d.oxygen_level == 0:
                d.has_health_issue = False
                d.renew_oxy()
                br+=1
        return f"Divers recovered: {br}"
    def diver_catch_report(self,diver_name: str):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        result = [f"**{diver_name} Catch Report**"]
        for f in diver.catch:
            result.append(f.fish_details())
        if not diver:
            return f"{diver_name} is not registered for the competition."
        return "\n".join(result)
    def competition_statistics(self):
        healthy = [d for d in self.divers if d.has_health_issue == False]
        divers = sorted(healthy, key=lambda d: (-d.competition_points, -len(d.catch), d.name.lower()))
        result = ["**Nautical Catch Challenge Statistics**"]
        for d in divers:
            result.append(d.__str__())
        return '\n'.join(result)
    #helping
    @staticmethod
    def ox_lvl(diver:BaseDiver):
        if diver.oxygen_level == 0:
            diver.has_health_issue = True

    @staticmethod
    def health_issue(diver:BaseDiver):
        if diver.has_health_issue:
            return f"{diver.name} will not be allowed to dive, due to health issues."


nautical_catch_challenge = NauticalCatchChallengeApp()

# Dive into competition
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

# Swim into competition
print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# Check health recovery
print(nautical_catch_challenge.health_recovery())

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# View catch reports
print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))

# View competition statistics
print(nautical_catch_challenge.competition_statistics())


