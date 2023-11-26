from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, given_player):
        if given_player in self.players:
            return f"Player {given_player.name} is already in the guild."

        elif given_player.guild != "Unaffiliated":
            return f"Player {given_player.name} is in another guild."

        else:
            self.players.append(given_player)
            given_player.guild = self.name
            return f"Welcome player {given_player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for player_str in self.players:
            if player_str.name == player_name:
                self.players.remove(player_str)
                player_str.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = "\n".join(single_player.player_info() for single_player in self.players)
        return f"Guild: {self.name}\n{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
